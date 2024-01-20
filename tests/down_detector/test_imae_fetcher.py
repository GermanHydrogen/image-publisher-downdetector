import asyncio
from unittest.mock import Mock

import pytest
from PIL import Image

from image_publish_downdetector.down_detector.image_fetcher import ImageFetcher


@pytest.mark.asyncio
async def test_image_fetcher_exception(mocker):
    mocker.patch("asyncio.sleep")
    image_fetcher = ImageFetcher("url")
    image_fetcher._fetch = Mock(side_effect=Exception)

    with pytest.raises(Exception):
        await image_fetcher()

    assert image_fetcher._fetch.call_count == 3
    assert asyncio.sleep.call_count == 3

@pytest.mark.asyncio
async def test_image_fetcher():
    image_fetcher = ImageFetcher("url")
    image = Image.new("RGB", (2, 2))
    image_fetcher._fetch = Mock(return_value=image)

    assert await image_fetcher() == image
