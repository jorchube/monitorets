import psutil

from .sampler import Sampler


class MemorySampler(Sampler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_sample(self):
        vmem = psutil.virtual_memory()

        available = vmem.available
        total = vmem.total
        used = total - available

        value = int((used/total) * 100)

        return value
