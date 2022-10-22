from .monitor_widget import MonitorWidget
from ..samplers.gpu_sampler import GpuSampler
from ..monitor_type import MonitorType
from . import colors


class GpuMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        title = "GPU"
        sampler = GpuSampler("/sys/class/drm/card0/device/gpu_busy_percent")
        type = MonitorType.GPU
        color = colors.GREEN

        super().__init__(title, sampler, type, color, *args, **kwargs)
