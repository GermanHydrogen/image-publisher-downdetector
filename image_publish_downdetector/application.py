import asyncio
from asyncio import Task
from typing import Optional

from image_publish_downdetector.down_detector import DownDetector
from image_publish_downdetector.notifier import Notifier


class Application(object):
    def __init__(self, down_detector: DownDetector, notifier: Notifier, notify_message_factory):
        self._down_detector = down_detector
        self._notifier = notifier
        self._notify_message_factory = notify_message_factory

        self._task: Optional[Task] = None

    def start(self):
        self._task = asyncio.create_task(self._loop())

    async def _loop(self):
        while True:
            self._iterate()

    def _iterate(self):
        try:
            state = self._down_detector
        except Exception as e:
            self._notifier.send_notification(f"DownDetector error: {e}")
            return

        if state is not None:
            notify_msg = self._notify_message_factory(state)
            self._notifier.send_notification(notify_msg)