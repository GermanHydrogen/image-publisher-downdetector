import asyncio
import sys
import yaml

from image_publish_downdetector.application import Application
from image_publish_downdetector.down_detector import DownDetector
from image_publish_downdetector.down_detector.image_cache_comparer import ImageCacheComparer
from image_publish_downdetector.down_detector.image_fetcher import ImageFetcher
from image_publish_downdetector.notifier import Notifier
from image_publish_downdetector.notifier.notify_message_factory import NotifyMessageFactory
from image_publish_downdetector.down_detector.state_switch import StateSwitch


def load_config(config_file_path: str):
    with open(config_file_path, "r") as file:
        return yaml.load(file, Loader=yaml.FullLoader)


async def main(config_file_path: str):
    config = load_config(config_file_path)

    image_fetcher = ImageFetcher(url=config["server"])
    image_cache_comparer = ImageCacheComparer()
    state_switch = StateSwitch()
    down_detector = DownDetector(image_fetcher, image_cache_comparer, state_switch)

    notifier = Notifier(topic=config["ntfy_topic"], server=config.get("ntfy_server", "https://ntfy.sh"))
    notify_message_factory = NotifyMessageFactory(service_name=config.get("service_name", "Service"))

    pull_time = config.get("pull_time")

    application = Application(down_detector, notifier, notify_message_factory, pull_time)
    await application.start()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python main.py [config file]')

    asyncio.run(main(sys.argv[1]))
