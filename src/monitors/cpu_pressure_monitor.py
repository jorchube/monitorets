from .monitor import Monitor
from ..samplers.cpu_pressure_sampler import CpuPressureSampler


class CpuPressureMonitor(Monitor):
    def __init__(self):
        sampler = CpuPressureSampler()
        super().__init__(sampler)
