from .monitor import Monitor
from ..samplers.gpu_sampler import GpuSampler

class GpuMonitor(Monitor):
    def __init__(self):
        sampler = GpuSampler("/sys/class/drm/card0/device/gpu_busy_percent")
        super().__init__(sampler)
