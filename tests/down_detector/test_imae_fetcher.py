from unittest.mock import Mock

import pytest
from PIL import Image

from image_publish_downdetector.down_detector.image_fetcher import ImageFetcher


def test_image_fetcher_exception():
    image_fetcher = ImageFetcher("url")
    image_fetcher._fetch = Mock(side_effect=Exception)

    with pytest.raises(Exception):
        image_fetcher()

    assert image_fetcher._fetch.call_count == 3


def test_image_fetcher():
    image_fetcher = ImageFetcher("url")
    image = Image.new("RGB", (2, 2))
    image_fetcher._fetch = Mock(return_value=image)

    assert image_fetcher() == image
