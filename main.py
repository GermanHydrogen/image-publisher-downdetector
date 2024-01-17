import asyncio

from image_publish_downdetector.application import Application
from image_publish_downdetector.config import Config
from image_publish_downdetector.down_detector import DownDetector
from image_publish_downdetector.down_detector.image_cache_comparer import ImageCacheComparer
from image_publish_downdetector.down_detector.image_fetcher import ImageFetcher
from image_publish_downdetector.down_detector.state_switch import StateSwitch
from image_publish_downdetector.notifier import Notifier
from image_publish_downdetector.notifier.notify_message_factory import NotifyMessageFactory


async def main():
    config = Config()

    image_fetcher = ImageFetcher(url=config.server)
    image_cache_comparer = ImageCacheComparer()
    state_switch = StateSwitch()
    down_detector = DownDetector(image_fetcher, image_cache_comparer, state_switch)

    notifier = Notifier(topic=config.nfty_topic, server=config.nfty_server)
    notify_message_factory = NotifyMessageFactory(service_name=config.service_name)

    pull_time = config.pull_time

    application = Application(down_detector, notifier, notify_message_factory, pull_time)
    await application.start()


if __name__ == '__main__':
    asyncio.run(main())
