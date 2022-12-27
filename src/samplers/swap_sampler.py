import psutil

from .sampler import Sampler


class SwapSampler(Sampler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_sample(self):
        swap = psutil.swap_memory()
        value = int(swap.percent)
        return value
