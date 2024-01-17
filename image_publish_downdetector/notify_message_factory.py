from image_publish_downdetector.state_switch import State


class NotifyMessageFactory:
    def __init__(self, service_name: str):
        self._service_name = service_name

    def __call__(self, state: State):
        if state == State.ONLINE:
            return f"{self._service_name} is online."
        else:
            return f"{self._service_name} is down."
