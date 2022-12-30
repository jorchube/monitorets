from .monitor import Monitor
from ..samplers.cpu_per_core_sampler import CpuPerCoreSampler


class CpuPerCoreMonitor(Monitor):
    def __init__(self):
        sampler = CpuPerCoreSampler()
        super().__init__(sampler)

    def _report_values(self):
        values = list(zip(*self._values))
        self._new_values_callback(values)
