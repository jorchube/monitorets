from .monitor_type import MonitorType
from .preference_keys import PreferenceKeys
from .ui.monitor_widgets.cpu_monitor_widget import CpuMonitorWidget
from .ui.monitor_widgets.gpu_monitor_widget import GpuMonitorWidget
from .ui.monitor_widgets.memory_monitor_widget import MemoryMonitorWidget
from .ui.monitor_widgets.downlink_monitor_widget import DownlinkMonitorWidget
from .ui.monitor_widgets.home_usage_monitor_widget import HomeUsageMonitorWidget
from .ui.monitor_widgets.root_usage_monitor_widget import RootUsageMonitorWidget



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
    {
        'type': MonitorType.Downlink,
        'enabled_preference_key': PreferenceKeys.DOWNLINK_MONITOR_ENABLED,
        'monitor_class': DownlinkMonitorWidget,
        'preference_toggle_label': 'Downlink',
    },
    {
        'type': MonitorType.Home_usage,
        'enabled_preference_key': PreferenceKeys.HOME_USAGE_MONITOR_ENABLED,
        'monitor_class': HomeUsageMonitorWidget,
        'preference_toggle_label': 'Home folder usage',
    },
    {
        'type': MonitorType.Root_usage,
        'enabled_preference_key': PreferenceKeys.ROOT_USAGE_MONITOR_ENABLED,
        'monitor_class': RootUsageMonitorWidget,
        'preference_toggle_label': 'Root folder usage',
    },
]
