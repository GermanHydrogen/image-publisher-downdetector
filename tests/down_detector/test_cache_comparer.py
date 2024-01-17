from PIL import Image

from image_publish_downdetector.down_detector.image_cache_comparer import ImageCacheComparer


def test_call_default() -> None:
    image = Image.new("RGB", (1, 1))
    cache = ImageCacheComparer()

    assert cache(image) == False
    assert cache._last_image == image


def test_is_different() -> None:
    last_image = Image.new("RGB", (2, 2))
    image = Image.new("RGB", (2, 2))
    image = image.point(lambda x: 255)

    cache = ImageCacheComparer()
    cache._last_image = last_image

    assert cache._is_different(image)
