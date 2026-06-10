from automata.states import State, INITIAL_STATE, FINAL_STATES
from automata.events import Event
from automata.transitions import get_next_state
from automata.transitions import TRANSITION_TABLE


class FsmEngine:
    def __init__(self) -> None:
        self._state: State = INITIAL_STATE

    def get_current_state(self) -> State:
        return self._state

    def transition(self, event: Event) -> State | None:
        if event == Event.SELESAI:
            self._state = State.END
            return State.END
        next_state = get_next_state(self._state, event)
        if next_state is not None:
            self._state = next_state
        return next_state

    def validate_transition(self, event: Event) -> bool:
        if event == Event.SELESAI:
            return True
        return get_next_state(self._state, event) is not None

    def reset(self) -> None:
        self._state = INITIAL_STATE

    def is_in_final_state(self) -> bool:
        return self._state in FINAL_STATES

    def get_all_states(self) -> list[State]:
        return list(State)

    def get_transition_table(self) -> dict[tuple[State, Event], State]:
        return dict(TRANSITION_TABLE)
