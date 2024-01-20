from typing import Optional

from image_publish_downdetector.down_detector.image_cache_comparer import ImageCacheComparer
from image_publish_downdetector.down_detector.image_fetcher import ImageFetcher
from image_publish_downdetector.down_detector.state_switch import StateSwitch, State


class DownDetector(object):
    def __init__(self,
                 image_fetcher: ImageFetcher,
                 image_cache: ImageCacheComparer,
                 state_switch: StateSwitch):

        self._image_fetcher = image_fetcher
        self._image_cache = image_cache
        self._state_switch = state_switch

    async def __call__(self) -> Optional[State]:
        new_image = await self._image_fetcher()
        has_changed = self._image_cache(new_image)
        state = State(int(has_changed))
        need_to_notify = self._state_switch.update(state)

        print(state)

        if need_to_notify:
            return state

        return None
