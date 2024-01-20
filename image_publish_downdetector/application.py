import asyncio

from image_publish_downdetector.down_detector import DownDetector
from image_publish_downdetector.notifier import Notifier


class Application(object):
    def __init__(self, down_detector: DownDetector, notifier: Notifier, notify_message_factory, sleep_time: int):
        self._down_detector = down_detector
        self._notifier = notifier
        self._notify_message_factory = notify_message_factory
        self._sleep_time = sleep_time

    async def start(self):
        self._notifier.send_notification("Started DownDetector.")
        await self._loop()

    async def _loop(self):
        while True:
            await self._looping()

    async def _looping(self):
        await self._iterate()
        await asyncio.sleep(self._sleep_time)

    async def _iterate(self):
        try:
            state = await self._down_detector()
        except Exception as e:
            self._notifier.send_notification(f"DownDetector error: {e}")
            return

        if state is not None:
            notify_msg = self._notify_message_factory(state)
            self._notifier.send_notification(notify_msg)
