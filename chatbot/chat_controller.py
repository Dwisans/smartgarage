from automata.events import Event
from automata.states import State
from chatbot.keyword_matcher import KeywordMatcher
from chatbot.response_generator import ResponseGenerator
from chatbot.session_manager import SessionManager

MODULE_MAP: dict[Event, str] = {
    Event.DIAGNOSA: "diagnosis",
    Event.SERVIS: "service",
    Event.TIPS: "maintenance",
}

MILEAGE_EVENTS: set[Event] = {
    Event.MILEAGE_5000, Event.MILEAGE_10000, Event.MILEAGE_15000,
    Event.MILEAGE_20000, Event.MILEAGE_25000,
}

MILEAGE_STATES: set[State] = {
    State.MOTOR_MILEAGE, State.MOBIL_MILEAGE,
}

VEHICLE_EVENTS: dict[Event, str] = {
    Event.MOTOR: "motor",
    Event.MOBIL: "mobil",
}

VEHICLE_STATES: dict[State, str] = {
    State.SELECT_MOTOR_SYMPTOM: "motor",
    State.SELECT_MOBIL_SYMPTOM: "mobil",
    State.MOTOR_MILEAGE: "motor",
    State.MOBIL_MILEAGE: "mobil",
}

RESULT_STATES: set[State] = {
    State.RESULT_ENGINE_MINOR, State.RESULT_ENGINE_MAJOR,
    State.RESULT_BATTERY_CHECK, State.RESULT_BATTERY_WEAK,
    State.RESULT_ELECTRICAL, State.RESULT_BRAKE, State.RESULT_TIRE,
    State.RESULT_TRANSMISI, State.RESULT_SUSPENSI, State.RESULT_PENDINGIN,
    State.SERVICE_5000, State.SERVICE_10000, State.SERVICE_15000,
    State.SERVICE_20000, State.SERVICE_25000,
    State.TIPS_ENGINE, State.TIPS_OIL, State.TIPS_BATTERY,
    State.TIPS_BRAKE, State.TIPS_TIRE,
    State.TIPS_TRANSMISI, State.TIPS_SUSPENSI, State.TIPS_PENDINGIN,
}

QUESTION_STATES: set[State] = {
    State.DIAGNOSIS_START, State.SELECT_MOTOR_SYMPTOM,
    State.SELECT_MOBIL_SYMPTOM, State.MOTOR_ENGINE,
    State.ENGINE_Q2, State.ENGINE_Q3,
    State.MOTOR_ELECTRICAL, State.MOTOR_BRAKE, State.MOTOR_TIRE,
    State.MOTOR_TRANSMISI, State.MOTOR_SUSPENSI, State.MOTOR_PENDINGIN,
    State.SERVICE_START, State.MOTOR_MILEAGE, State.MOBIL_MILEAGE,
    State.MAINTENANCE_VEHICLE, State.MAINTENANCE_START,
}


class ChatController:
    def __init__(self) -> None:
        self.matcher = KeywordMatcher()
        self.generator = ResponseGenerator()

    MODULE_QUESTION_STATES: dict[str, set[State]] = {
        "diagnosis": {
            State.DIAGNOSIS_START, State.SELECT_MOTOR_SYMPTOM,
            State.SELECT_MOBIL_SYMPTOM, State.MOTOR_ENGINE,
            State.ENGINE_Q2, State.ENGINE_Q3,
            State.MOTOR_ELECTRICAL, State.MOTOR_BRAKE, State.MOTOR_TIRE,
            State.MOTOR_TRANSMISI, State.MOTOR_SUSPENSI, State.MOTOR_PENDINGIN,
        },
        "service": {
            State.SERVICE_START, State.MOTOR_MILEAGE, State.MOBIL_MILEAGE,
        },
        "maintenance": {
            State.MAINTENANCE_VEHICLE, State.MAINTENANCE_START,
        },
    }

    def process_input(self, session: SessionManager, user_input: str) -> str:
        session.add_message("user", user_input)
        event = self.matcher.match(user_input)
        current = session.fsm.get_current_state()

        # ── START -> WELCOME ──
        if event == Event.START_CHAT and current == State.START:
            session.fsm.transition(event)
            response = self.generator.generate(session.fsm.get_current_state())
            session.add_message("bot", response)
            return response

        # ── UNKNOWN input ──
        if event == Event.UNKNOWN:
            response = self._unknown_response(current)
            session.add_message("bot", response)
            return response

        # ── Context-aware: re-match when module keyword fires inside its own flow ──
        if event in MODULE_MAP and current in self.MODULE_QUESTION_STATES.get(MODULE_MAP[event], set()):
            from chatbot.keyword_matcher import MODULE_EVENTS
            event = self.matcher.match_excluding(user_input, MODULE_EVENTS)

        # ── Context-aware: at symptom selection state, prefer symptom keyword over YA/TIDAK ──
        SYMPTOM_EVENTS = {Event.MESIN, Event.KELISTRIKAN, Event.AKI, Event.REM, Event.BAN,
                          Event.TRANSMISI, Event.SUSPENSI, Event.PENDINGIN}
        if event in (Event.YA, Event.TIDAK) and current in (State.SELECT_MOTOR_SYMPTOM, State.SELECT_MOBIL_SYMPTOM):
            re = self.matcher.match_excluding(user_input, {Event.YA, Event.TIDAK})
            if re in SYMPTOM_EVENTS:
                event = re

        # ── Context-aware: at answer state, symptom keyword = YA ──
        ANSWER_STATES = {
            State.MOTOR_ENGINE, State.ENGINE_Q2, State.ENGINE_Q3,
            State.MOTOR_ELECTRICAL, State.MOTOR_BRAKE, State.MOTOR_TIRE,
            State.MOTOR_TRANSMISI, State.MOTOR_SUSPENSI, State.MOTOR_PENDINGIN,
        }
        if current in ANSWER_STATES and event in SYMPTOM_EVENTS:
            event = Event.YA

        # ── Context-aware: at mileage state, prefer numeric match ──
        MILEAGE_STATES = {State.MOTOR_MILEAGE, State.MOBIL_MILEAGE}
        if current in MILEAGE_STATES:
            from chatbot.keyword_matcher import MILEAGE_EVENTS, MILEAGE_RANGES
            digits = "".join(c for c in user_input if c.isdigit())
            if digits and len(digits) >= 4:
                num = int(digits)
                for mval, mev in MILEAGE_EVENTS:
                    if num == mval:
                        event = mev
                        break
                if event not in [mev for _, mev in MILEAGE_EVENTS]:
                    for mrange, mev in MILEAGE_RANGES:
                        if num in mrange:
                            event = mev
                            break

        # ── Track module & vehicle ──
        if module := MODULE_MAP.get(event):
            session.current_module = module
        if vehicle := VEHICLE_EVENTS.get(event):
            session.current_vehicle = vehicle
        if current in VEHICLE_STATES:
            session.current_vehicle = VEHICLE_STATES[current]

        # ── MENU: back to welcome ──
        if event == Event.MENU:
            session.fsm.reset()
            session.fsm.transition(Event.START_CHAT)
            response = self.generator.generate(session.fsm.get_current_state())
            session.add_message("bot", response)
            return response

        # ── SELESAI: end conversation ──
        if event == Event.SELESAI:
            session.fsm.transition(Event.SELESAI)
            response = self.generator.generate(State.END)
            session.add_message("bot", response)
            return response

        # ── Valid transition via FSM table ──
        if session.fsm.validate_transition(event):
            session.fsm.transition(event)
            response = self.generator.generate(
                session.fsm.get_current_state(),
                vehicle=session.current_vehicle,
            )
            session.add_message("bot", response)
            return response

        # ── Invalid: give contextual help without resetting ──
        response = self._invalid_response(current, event)
        session.add_message("bot", response)
        return response

    def _unknown_response(self, current: State) -> str:
        if current == State.START:
            return "Halo, ketik **halo** atau **mulai** untuk ngobrol, ya."
        if current in RESULT_STATES:
            return (
                "Maaf, aku kurang paham. Ketik **menu** kalau mau "
                "kembali ke menu utama atau **selesai** kalau sudah cukup."
            )
        if current in QUESTION_STATES:
            return (
                "Maaf, aku kurang paham. Coba jawab sesuai pilihan "
                "yang tersedia, atau ketik **menu** untuk kembali."
            )
        if current == State.WELCOME:
            return (
                "Silakan pilih salah satu:\n"
                "- **Diagnosa** \u2014 cari tahu masalah kendaraan\n"
                "- **Servis** \u2014 jadwal perawatan\n"
                "- **Tips** \u2014 panduan perawatan"
            )
        return "Maaf, aku kurang paham. Ketik **menu** untuk kembali."

    def _invalid_response(self, current: State, event: Event) -> str:
        if current in RESULT_STATES and event in MODULE_MAP:
            return (
                "Sepertinya ada sedikit kekeliruan. "
                "Ketik **menu** untuk memilih layanan yang benar."
            )
        if event in MILEAGE_EVENTS:
            if current == State.SERVICE_START:
                return "Kamu harus pilih **motor** atau **mobil** dulu sebelum memasukkan KM."
            if current not in MILEAGE_STATES:
                return (
                    "Kamu sedang tidak di menu servis. "
                    "Ketik **menu** lalu pilih **Servis** untuk "
                    "cek jadwal berdasarkan KM."
                )
        return self._unknown_response(current)
