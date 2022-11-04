from .monitor_type import MonitorType
from .ui.cpu_monitor_widget import CpuMonitorWidget
from .ui.gpu_monitor_widget import GpuMonitorWidget
from .ui.memory_monitor_widget import MemoryMonitorWidget


monitor_descriptor_list = [
    {
        'type': MonitorType.CPU,
        'enabled_preference_key': "cpu_monitor.enabled",
        'monitor_class': CpuMonitorWidget,
    },
    {
        'type': MonitorType.GPU,
        'enabled_preference_key': "gpu_monitor.enabled",
        'monitor_class': GpuMonitorWidget,
    },
    {
        'type': MonitorType.Memory,
        'enabled_preference_key': "memory_monitor.enabled",
        'monitor_class': MemoryMonitorWidget,
    },
]
