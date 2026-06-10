from automata.fsm_engine import FsmEngine
from automata.states import State


class SessionManager:
    def __init__(self) -> None:
        self.fsm = FsmEngine()
        self.chat_history: list[dict[str, str]] = []
        self.current_module: str = ""
        self.current_vehicle: str = ""
        self.conversation_context: dict[str, str] = {}

    def add_message(self, sender: str, message: str) -> None:
        self.chat_history.append({"sender": sender, "message": message})

    def reset(self) -> None:
        self.fsm.reset()
        self.chat_history.clear()
        self.current_module = ""
        self.current_vehicle = ""
        self.conversation_context = {}

    def to_dict(self) -> dict:
        return {
            "current_state": self.fsm.get_current_state().name,
            "current_module": self.current_module,
            "current_vehicle": self.current_vehicle,
            "conversation_context": self.conversation_context,
            "chat_history": self.chat_history,
        }
