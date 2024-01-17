from PIL import Image
import requests
from io import BytesIO


class ImageFetcher:
    def __init__(self, url: str):
        self._url = url

    def __call__(self) -> Image:
        response = requests.get(url=self._url)
        img = Image.open(BytesIO(response.content))

        return img
