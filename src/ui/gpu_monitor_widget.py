from .monitor_widget import MonitorWidget
from ..samplers.gpu_sampler import GpuSampler
from . import colors


class GpuMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        title = "GPU"
        sampler = GpuSampler("/sys/class/drm/card0/device/gpu_busy_percent")
        color = colors.GREEN

        super().__init__(title, sampler, color, *args, **kwargs)
