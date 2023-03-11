from .monitor import Monitor
from ..samplers.memory_pressure_sampler import MemoryPressureSampler


class MemoryPressureMonitor(Monitor):
    def __init__(self):
        sampler = MemoryPressureSampler()
        super().__init__(sampler)
