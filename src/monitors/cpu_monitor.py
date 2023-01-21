from .monitor import Monitor
from ..samplers.cpu_sampler import CpuSampler


class CpuMonitor(Monitor):
    def __init__(self):
        sampler = CpuSampler()
        super().__init__(sampler)
