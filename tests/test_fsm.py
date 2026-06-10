import pytest
from automata.fsm_engine import FsmEngine
from automata.states import State, INITIAL_STATE, FINAL_STATES
from automata.events import Event
from automata.transitions import TRANSITION_TABLE, get_next_state


class TestFsmEngine:
    def setup_method(self) -> None:
        self.fsm = FsmEngine()

    def test_initial_state(self) -> None:
        assert self.fsm.get_current_state() == INITIAL_STATE

    def test_transition_to_welcome(self) -> None:
        result = self.fsm.transition(Event.START_CHAT)
        assert result == State.WELCOME
        assert self.fsm.get_current_state() == State.WELCOME

    def test_full_diagnosis_flow_motor_engine_yes(self) -> None:
        steps = [
            (Event.START_CHAT, State.WELCOME),
            (Event.DIAGNOSA, State.DIAGNOSIS_START),
            (Event.MOTOR, State.SELECT_MOTOR_SYMPTOM),
            (Event.MESIN, State.MOTOR_ENGINE),
            (Event.YA, State.ENGINE_Q2),
            (Event.YA, State.RESULT_ENGINE_MINOR),
        ]
        for event, expected in steps:
            result = self.fsm.transition(event)
            assert result == expected, f"Failed on event {event}: got {result}, expected {expected}"

    def test_full_diagnosis_flow_motor_engine_no_starter(self) -> None:
        steps = [
            (Event.START_CHAT, State.WELCOME),
            (Event.DIAGNOSA, State.DIAGNOSIS_START),
            (Event.MOTOR, State.SELECT_MOTOR_SYMPTOM),
            (Event.MESIN, State.MOTOR_ENGINE),
            (Event.TIDAK, State.ENGINE_Q3),
            (Event.TIDAK, State.RESULT_BATTERY_WEAK),
        ]
        for event, expected in steps:
            result = self.fsm.transition(event)
            assert result == expected, f"Failed on event {event}"

    def test_full_service_flow(self) -> None:
        steps = [
            (Event.START_CHAT, State.WELCOME),
            (Event.SERVIS, State.SERVICE_START),
            (Event.MOTOR, State.MOTOR_MILEAGE),
            (Event.MILEAGE_10000, State.SERVICE_10000),
        ]
        for event, expected in steps:
            result = self.fsm.transition(event)
            assert result == expected, f"Failed on event {event}"

    def test_full_maintenance_flow(self) -> None:
        steps = [
            (Event.START_CHAT, State.WELCOME),
            (Event.TIPS, State.MAINTENANCE_VEHICLE),
            (Event.MOTOR, State.MAINTENANCE_START),
            (Event.OLI, State.TIPS_OIL),
        ]
        for event, expected in steps:
            result = self.fsm.transition(event)
            assert result == expected, f"Failed on event {event}"

    def test_invalid_transition(self) -> None:
        self.fsm.transition(Event.START_CHAT)
        self.fsm.transition(Event.DIAGNOSA)
        assert self.fsm.get_current_state() == State.DIAGNOSIS_START
        result = self.fsm.transition(Event.MILEAGE_10000)
        assert result is None

    def test_validate_transition(self) -> None:
        assert self.fsm.validate_transition(Event.START_CHAT)
        assert not self.fsm.validate_transition(Event.MILEAGE_5000)

    def test_reset(self) -> None:
        self.fsm.transition(Event.START_CHAT)
        self.fsm.transition(Event.DIAGNOSA)
        self.fsm.reset()
        assert self.fsm.get_current_state() == INITIAL_STATE

    def test_is_in_final_state(self) -> None:
        assert not self.fsm.is_in_final_state()
        self.fsm._state = State.END
        assert self.fsm.is_in_final_state()

    def test_get_all_states_includes_all(self) -> None:
        all_states = self.fsm.get_all_states()
        for s in State:
            assert s in all_states

    def test_transition_table_has_all_expected_entries(self) -> None:
        expected_transitions = [
            (State.START, Event.START_CHAT, State.WELCOME),
            (State.WELCOME, Event.DIAGNOSA, State.DIAGNOSIS_START),
            (State.WELCOME, Event.SERVIS, State.SERVICE_START),
            (State.WELCOME, Event.TIPS, State.MAINTENANCE_VEHICLE),
            (State.DIAGNOSIS_START, Event.MOTOR, State.SELECT_MOTOR_SYMPTOM),
            (State.MOTOR_ENGINE, Event.YA, State.ENGINE_Q2),
            (State.MOTOR_ENGINE, Event.TIDAK, State.ENGINE_Q3),
        ]
        for current, event, expected in expected_transitions:
            result = get_next_state(current, event)
            assert result == expected, f"Missing/incorrect: ({current.name}, {event.name}) -> {expected}"

    def test_end_state_has_no_outgoing(self) -> None:
        for event in Event:
            result = get_next_state(State.END, event)
            assert result is None, f"END state should not transition on {event.name}"
