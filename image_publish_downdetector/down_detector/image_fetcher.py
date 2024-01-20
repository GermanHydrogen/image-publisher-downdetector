import asyncio

from PIL import Image
import requests
from io import BytesIO


class ImageFetcher:
    MAX_FAILURES = 3
    WAIT_AFTER_FAILURE = 10

    def __init__(self, url: str):
        self._url = url

    async def __call__(self) -> Image:
        failures = 0
        exception: Exception
        while failures < self.MAX_FAILURES:
            try:
                return self._fetch()
            except Exception as exception:
                failures += 1
                await asyncio.sleep(self.WAIT_AFTER_FAILURE)

        raise exception

    def _fetch(self) -> Image:
        response = requests.get(url=self._url)
        img = Image.open(BytesIO(response.content))

        return img