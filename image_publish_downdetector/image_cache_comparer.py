from PIL import Image
from typing import Optional


class ImageCacheComparer(object):
    def __init__(self) -> None:
        self._last_image: Optional[Image] = None

    def __call__(self, image: Image) -> bool:
        is_different = self._is_different(image)
        self._save(image)

        return is_different

    def _is_different(self, image: Image) -> bool:
        if self._last_image is None:
            return False

        diff = self._last_image.difference(image)

        if diff.getbbox():
            return True

        return False

    def _save(self, image: Image) -> None:
        self._last_image = image