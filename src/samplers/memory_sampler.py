import psutil

from .sampler import Sampler


class MemorySampler(Sampler):
    def __init__(self):
        super().__init__()

    def _get_sample(self):
        vmem = psutil.virtual_memory()

        available = vmem.available
        total = vmem.total

        value = int((available/total) * 100)

        return value
