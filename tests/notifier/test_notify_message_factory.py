from image_publish_downdetector.down_detector.state_switch import State
from image_publish_downdetector.notifier.notify_message_factory import NotifyMessageFactory


def test_online():
    factory = NotifyMessageFactory("test")
    assert factory(State.ONLINE) == "test is online."


def test_offline():
    factory = NotifyMessageFactory("test")
    assert factory(State.OFFLINE) == "test is down."
