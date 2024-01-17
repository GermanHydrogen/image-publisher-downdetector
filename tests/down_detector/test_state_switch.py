from image_publish_downdetector.down_detector.state_switch import StateSwitch, State


def test_state_switch_default():
    state_switch = StateSwitch()
    assert state_switch._state == State.OFFLINE


def test_state_update_different():
    state_switch = StateSwitch(State.ONLINE)

    assert state_switch.update(State.OFFLINE)
    assert state_switch._state == State.OFFLINE


def test_state_update_same():
    state_switch = StateSwitch(State.ONLINE)

    assert not state_switch.update(State.ONLINE)
    assert state_switch._state == State.ONLINE
