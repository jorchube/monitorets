from .monitor import Monitor
from ..samplers.swap_sampler import SwapSampler

class SwapMonitor(Monitor):
    def __init__(self):
        sampler = SwapSampler()
        super().__init__(sampler)
