from .monitor_type import MonitorType
from .ui.cpu_monitor_widget import CpuMonitorWidget
from .ui.gpu_monitor_widget import GpuMonitorWidget
from .ui.memory_monitor_widget import MemoryMonitorWidget
from .preferences import PreferenceKeys


monitor_descriptor_list = [
    {
        'type': MonitorType.CPU,
        'enabled_preference_key': PreferenceKeys.CPU_MONITOR_ENABLED,
        'monitor_class': CpuMonitorWidget,
        'preference_toggle_label': 'CPU',
    },
    {
        'type': MonitorType.GPU,
        'enabled_preference_key': PreferenceKeys.GPU_MONITOR_ENABLED,
        'monitor_class': GpuMonitorWidget,
        'preference_toggle_label': 'GPU (experimental)',
    },
    {
        'type': MonitorType.Memory,
        'enabled_preference_key': PreferenceKeys.MEMORY_MONITOR_ENABLED,
        'monitor_class': MemoryMonitorWidget,
        'preference_toggle_label': 'Memory',
    },
]
