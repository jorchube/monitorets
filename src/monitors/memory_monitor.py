from .monitor import Monitor
from ..samplers.memory_sampler import MemorySampler

class MemoryMonitor(Monitor):
    def __init__(self):
        sampler = MemorySampler()
        super().__init__(sampler)
