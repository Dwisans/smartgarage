from enum import Enum, auto


class State(Enum):
    START = auto()
    WELCOME = auto()
    MAIN_MENU = auto()

    DIAGNOSIS_START = auto()
    SELECT_MOTOR_SYMPTOM = auto()
    SELECT_MOBIL_SYMPTOM = auto()
    MOTOR_ENGINE = auto()
    ENGINE_Q2 = auto()
    ENGINE_Q3 = auto()
    MOTOR_ELECTRICAL = auto()
    MOTOR_BRAKE = auto()
    MOTOR_TIRE = auto()
    MOTOR_TRANSMISI = auto()
    MOTOR_SUSPENSI = auto()
    MOTOR_PENDINGIN = auto()
    RESULT_ENGINE_MINOR = auto()
    RESULT_ENGINE_MAJOR = auto()
    RESULT_BATTERY_CHECK = auto()
    RESULT_BATTERY_WEAK = auto()
    RESULT_ELECTRICAL = auto()
    RESULT_BRAKE = auto()
    RESULT_TIRE = auto()
    RESULT_TRANSMISI = auto()
    RESULT_SUSPENSI = auto()
    RESULT_PENDINGIN = auto()

    SERVICE_START = auto()
    MOTOR_MILEAGE = auto()
    MOBIL_MILEAGE = auto()
    SERVICE_5000 = auto()
    SERVICE_10000 = auto()
    SERVICE_15000 = auto()
    SERVICE_20000 = auto()
    SERVICE_25000 = auto()

    MAINTENANCE_VEHICLE = auto()
    MAINTENANCE_START = auto()
    TIPS_ENGINE = auto()
    TIPS_OIL = auto()
    TIPS_BATTERY = auto()
    TIPS_BRAKE = auto()
    TIPS_TIRE = auto()
    TIPS_TRANSMISI = auto()
    TIPS_SUSPENSI = auto()
    TIPS_PENDINGIN = auto()

    END = auto()


INITIAL_STATE = State.START
FINAL_STATES = {State.END}
