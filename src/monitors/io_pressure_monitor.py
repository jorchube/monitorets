from .monitor import Monitor
from ..samplers.io_pressure_sampler import IOPressureSampler


class IOPressureMonitor(Monitor):
    def __init__(self):
        sampler = IOPressureSampler()
        super().__init__(sampler)
