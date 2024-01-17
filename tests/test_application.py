import asyncio
from unittest.mock import Mock

import pytest

from image_publish_downdetector.application import Application
from image_publish_downdetector.down_detector.state_switch import State
from image_publish_downdetector.notifier import Notifier


def test_iterate_error():
    down_detector = Mock(side_effect=ValueError("Test"))
    notify = Notifier("", "")
    notify.send_notification = Mock()

    app = Application(down_detector, notify, None, 10)

    app._iterate()

    notify.send_notification.assert_called_once_with("DownDetector error: Test")


def test_iterate_notify():
    down_detector = Mock(return_value=State.ONLINE)
    notify = Notifier("", "")
    notify.send_notification = Mock()
    msg_factory = Mock(return_value="Test")

    app = Application(down_detector, notify, msg_factory, 10)

    app._iterate()

    msg_factory.assert_called_once_with(State.ONLINE)
    notify.send_notification.assert_called_once_with("Test")


@pytest.mark.asyncio
async def test_start(mocker):
    notify = Notifier("", "")
    notify.send_notification = Mock()

    app = Application(None, notify, None, 10)
    mocker.patch.object(app, "_loop")

    await app.start()

    notify.send_notification.assert_called_once_with("Started DownDetector.")
    app._loop.assert_called_once()


@pytest.mark.asyncio
async def test_looping(mocker):
    mocker.patch("asyncio.sleep")
    app = Application(None, None, None, 10)
    mocker.patch.object(app, "_iterate")

    await app._looping()

    asyncio.sleep.assert_called_once_with(10)
    app._iterate.assert_called_once()

