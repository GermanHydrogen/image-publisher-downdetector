from enum import Enum


class State(Enum):
    ONLINE = 1
    OFFLINE = 0


class SwitchState(object):
    def __init__(self, initial_state: State = State.OFFLINE):
        self._state = initial_state

    def update(self, new_state: State) -> bool:
        if new_state == self._state:
            return False

        self._state = new_state
        return True
