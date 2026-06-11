from automata.states import State
from data.diagnosis_data import DIAGNOSIS_DATA
from data.service_data import SERVICE_DATA
from data.maintenance_data import MAINTENANCE_DATA

MOTOR_SYMPTOM_OPTIONS = (
    "- **Mesin**: brebet, susah hidup, tarikan berat, overheat\n"
    "- **Transmisi**: gigi susah masuk, kopling selip, bunyi\n"
    "- **Kelistrikan**: lampu mati, aki soak, klakson mati\n"
    "- **Pendingin**: mesin overheat, radiator bocor\n"
    "- **Rem**: kurang pakem, bunyi, getaran saat ngerem\n"
    "- **Suspensi**: guncangan keras, motor oleng, shock bocor\n"
    "- **Ban**: bocor, aus gak rata, tekanan kurang"
)

MOBIL_SYMPTOM_OPTIONS = (
    "- **Mesin**: brebet, susah hidup, tarikan berat, overheat\n"
    "- **Transmisi**: gigi susah masuk, kopling selip, bunyi\n"
    "- **Kelistrikan**: lampu mati, aki soak, klakson mati\n"
    "- **Pendingin**: mesin overheat, radiator bocor, AC tidak dingin\n"
    "- **Rem**: kurang pakem, bunyi, getaran saat ngerem\n"
    "- **Suspensi**: guncangan keras, mobil oleng, shock bocor\n"
    "- **Ban**: bocor, aus gak rata, tekanan kurang"
)

STATE_RESPONSES: dict[State, str] = {
    State.WELCOME: (
        "Halo, aku AutoCare Assistant.\n\n"
        "Aku bisa bantu kamu:\n"
        "- **Diagnosa** \u2014 cari tahu masalah kendaraanmu\n"
        "- **Servis** \u2014 lihat jadwal perawatan berkala\n"
        "- **Tips** \u2014 panduan merawat kendaraan\n\n"
        "Mau mulai dari mana?"
    ),
    State.DIAGNOSIS_START: (
        "Oke, kita cari tahu dulu masalah kendaraanmu.\n"
        "Kendaraanmu motor atau mobil?"
    ),
    State.SELECT_MOTOR_SYMPTOM: (
        "Motor ya. Sekarang cerita, gejala apa yang kamu rasakan?\n\n"
        + MOTOR_SYMPTOM_OPTIONS + "\n\n"
        "Ketik gejala yang kamu alami, ya."
    ),
    State.SELECT_MOBIL_SYMPTOM: (
        "Mobil ya. Coba cerita, gejala apa yang kamu rasakan?\n\n"
        + MOBIL_SYMPTOM_OPTIONS + "\n\n"
        "Ketik gejala yang kamu alami, ya."
    ),
    State.MOTOR_ENGINE: (
        "Coba cek, starter motormu masih berfungsi atau mati total? (ya/tidak)"
    ),
    State.ENGINE_Q2: (
        "Kalau distarter, suara mesinnya normal atau bunyi aneh? (ya/tidak)"
    ),
    State.ENGINE_Q3: (
        "Lampu indikator di dashboard nyala atau mati semua? (ya/tidak)"
    ),
    State.MOTOR_ELECTRICAL: (
        "Apakah yang bermasalah hanya satu lampu/komponen saja, "
        "atau beberapa komponen listrik mati sekaligus? (ya = satu saja / tidak = beberapa sekaligus)"
    ),
    State.MOTOR_BRAKE: (
        "Apakah rem terasa kurang pakem atau bunyi saat dipakai? (ya/tidak)"
    ),
    State.MOTOR_TIRE: (
        "Apakah ban sering bocor atau ausnya gak merata? (ya/tidak)"
    ),
    State.MOTOR_TRANSMISI: (
        "Apa yang kamu rasakan: gigi susah masuk, kopling selip, "
        "atau ada bunyi dari area transmisi? (ya/tidak)"
    ),
    State.MOTOR_SUSPENSI: (
        "Apa kendaraan terasa oleng, keras saat lewat jalan tidak rata, "
        "atau shockbreaker bunyi? (ya/tidak)"
    ),
    State.SERVICE_START: (
        "Mau cek jadwal servis untuk motor atau mobil?"
    ),
    State.MOTOR_MILEAGE: (
        "Sudah berapa KM kendaraanmu? Pilih salah satu:\n"
        "- 5.000 km\n"
        "- 10.000 km\n"
        "- 15.000 km\n"
        "- 20.000 km\n"
        "- 25.000 km"
    ),
    State.MOBIL_MILEAGE: (
        "Sudah berapa KM mobilmu? Pilih salah satu:\n"
        "- 5.000 km\n"
        "- 10.000 km\n"
        "- 15.000 km\n"
        "- 20.000 km\n"
        "- 25.000 km"
    ),
    State.MAINTENANCE_VEHICLE: (
        "Mau tips perawatan untuk motor atau mobil?"
    ),

}


def get_diagnosis_result(state: State, vehicle: str = "motor") -> str:
    key = state.name
    # Pendingin mobil → fokus AC, motor → fokus overheat/radiator
    if key == "RESULT_PENDINGIN" and vehicle == "mobil":
        key = "RESULT_PENDINGIN_AC"
    data = DIAGNOSIS_DATA.get(key)
    if not data:
        return "Oke, data diagnosisnya udah tercatat. Semoga cepet beres, ya."
    return (
        f"**{data['title']}**\n\n"
        f"{data['solution']}"
    )


def get_service_result(state: State, vehicle: str = "motor") -> str:
    mileages = {
        State.SERVICE_5000: "5000",
        State.SERVICE_10000: "10000",
        State.SERVICE_15000: "15000",
        State.SERVICE_20000: "20000",
        State.SERVICE_25000: "25000",
    }
    mileage_key = mileages.get(state)
    if not mileage_key:
        return "Hmm, rekomendasi servisnya gak ditemukan. Coba cek lagi, ya."
    items = SERVICE_DATA.get(vehicle, {}).get(mileage_key, [])
    if not items:
        return f"Untuk {mileage_key} km belum ada data servisnya. Coba pilih KM lain."
    items_str = "\n".join(f"- {item}" for item in items)
    return (
        f"Rekomendasi Servis {mileage_key} km ({vehicle})\n\n"
        f"{items_str}"
    )


def get_maintenance_result(state: State, vehicle: str = "motor") -> str:
    topic_map = {
        State.TIPS_ENGINE: "mesin",
        State.TIPS_OIL: "oli",
        State.TIPS_BATTERY: "aki",
        State.TIPS_BRAKE: "rem",
        State.TIPS_TIRE: "ban",
        State.TIPS_TRANSMISI: "transmisi",
        State.TIPS_SUSPENSI: "suspensi",
        State.TIPS_PENDINGIN: "pendingin",
    }
    topic = topic_map.get(state)
    if not topic:
        return "Tipsnya gak ditemukan. Coba pilih topik lain."

    # Pendingin mobil pakai data yang include tips AC
    data_key = "pendingin_mobil" if topic == "pendingin" and vehicle == "mobil" else topic

    items = MAINTENANCE_DATA.get(data_key, [])
    if not items:
        return f"Belum ada tips buat {topic}, nanti kita update."
    items_str = "\n".join(f"- {item}" for item in items)
    return (
        f"Tips Perawatan {topic.capitalize()} ({vehicle})\n\n"
        f"{items_str}"
    )


DIAGNOSIS_RESULT_STATES = {
    State.RESULT_ENGINE_MINOR,
    State.RESULT_ENGINE_MAJOR,
    State.RESULT_BATTERY_CHECK,
    State.RESULT_BATTERY_WEAK,
    State.RESULT_ELECTRICAL,
    State.RESULT_BRAKE,
    State.RESULT_TIRE,
    State.RESULT_TRANSMISI,
    State.RESULT_SUSPENSI,
    State.RESULT_PENDINGIN,
}
SERVICE_RESULT_STATES = {
    State.SERVICE_5000,
    State.SERVICE_10000,
    State.SERVICE_15000,
    State.SERVICE_20000,
    State.SERVICE_25000,
}
MAINTENANCE_RESULT_STATES = {
    State.TIPS_ENGINE,
    State.TIPS_OIL,
    State.TIPS_BATTERY,
    State.TIPS_BRAKE,
    State.TIPS_TIRE,
    State.TIPS_TRANSMISI,
    State.TIPS_SUSPENSI,
    State.TIPS_PENDINGIN,
}

ASK_AGAIN = "\n\n---\nAda lagi yang bisa aku bantu? Ketik **menu** atau **selesai**, ya."


class ResponseGenerator:
    def generate(self, state: State, vehicle: str = "motor") -> str:
        if state == State.MAINTENANCE_START:
            pendingin = "AC dan radiator" if vehicle == "mobil" else "radiator dan sistem pendingin"
            return (
                "Mau tips perawatan bagian apa?\n\n"
                "- **Mesin**: biar awet dan bertenaga\n"
                "- **Oli**: pilih dan ganti yang tepat\n"
                "- **Aki**: rawat biar gak tekor\n"
                "- **Transmisi**: jaga kopling dan gigi\n"
                "- **Rem**: safety first\n"
                "- **Suspensi**: handling tetap stabil\n"
                f"- **Pendingin**: {pendingin}\n"
                "- **Ban**: biar gak bocor terus\n\n"
                "Ketik pilihannya, ya."
            )

        if state == State.MOTOR_PENDINGIN:
            if vehicle == "mobil":
                return (
                    "Apa yang kamu rasakan: mesin cepat panas, indikator suhu naik, "
                    "radiator bocor, atau AC tidak dingin? (ya/tidak)"
                )
            return (
                "Apa yang kamu rasakan: mesin cepat panas, indikator suhu naik, "
                "atau radiator bocor? (ya/tidak)"
            )

        base = STATE_RESPONSES.get(state)
        if base:
            return base

        if state in DIAGNOSIS_RESULT_STATES:
            return get_diagnosis_result(state, vehicle) + ASK_AGAIN

        if state in SERVICE_RESULT_STATES:
            return get_service_result(state, vehicle) + ASK_AGAIN

        if state in MAINTENANCE_RESULT_STATES:
            return get_maintenance_result(state, vehicle) + ASK_AGAIN

        if state == State.END:
            return (
                "Terima kasih, ya. Semoga kendaraanmu selalu sehat.\n"
                "Kalau butuh bantuan lagi, tinggal chat aja."
            )

        if state == State.START:
            return "Halo, ketik **mulai** atau **halo** untuk ngobrol, ya."

        return (
            "Maaf, aku kurang paham maksudnya.\n"
            "Coba tanya dengan kata lain, atau ketik **menu**."
        )