from unittest.mock import Mock

from PIL import Image

from image_publish_downdetector.down_detector import DownDetector
from image_publish_downdetector.down_detector.state_switch import State, StateSwitch


def test_call_change():
    image = Image.new("RGB", (2, 2))
    image_fetcher = Mock(return_value=image)
    image_cache = Mock(return_value=True)
    state_switch = Mock(return_value=True)

    detector = DownDetector(image_fetcher, image_cache, state_switch)
    assert detector() == State.ONLINE


def test_call_no_change():
    image = Image.new("RGB", (2, 2))
    image_fetcher = Mock(return_value=image)
    image_cache = Mock(return_value=True)
    state_switch = StateSwitch()
    state_switch.update = Mock(return_value=False)

    detector = DownDetector(image_fetcher, image_cache, state_switch)
    assert detector() is None

    image_fetcher.assert_called_once()
    image_cache.assert_called_once_with(image)
    state_switch.update.assert_called_once_with(State.ONLINE)
