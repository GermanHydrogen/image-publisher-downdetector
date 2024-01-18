from PIL import Image
import requests
from io import BytesIO


class ImageFetcher:
    MAX_FAILURES = 3

    def __init__(self, url: str):
        self._url = url

    def __call__(self) -> Image:
        failures = 0
        exception: Exception
        while failures < self.MAX_FAILURES:
            try:
                return self._fetch()
            except Exception as exception:
                failures += 1

        raise exception

    def _fetch(self) -> Image:
        response = requests.get(url=self._url)
        img = Image.open(BytesIO(response.content))

        return img