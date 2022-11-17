from collections import defaultdict

from .monitor_type import MonitorType
from .preference_keys import PreferenceKeys
from .ui.monitor_widgets.cpu_monitor_widget import CpuMonitorWidget
from .ui.monitor_widgets.gpu_monitor_widget import GpuMonitorWidget
from .ui.monitor_widgets.memory_monitor_widget import MemoryMonitorWidget
from .ui.monitor_widgets.downlink_monitor_widget import DownlinkMonitorWidget
from .ui.monitor_widgets.uplink_monitor_widget import UplinkMonitorWidget
from .ui.monitor_widgets.home_usage_monitor_widget import HomeUsageMonitorWidget
from .ui.monitor_widgets.root_usage_monitor_widget import RootUsageMonitorWidget



monitor_descriptor_list = [
    {
        'type': MonitorType.CPU,
        'enabled_preference_key': PreferenceKeys.CPU_MONITOR_ENABLED,
        'monitor_class': CpuMonitorWidget,
        'preference_toggle_label': 'CPU',
        'preference_toggle_section_name': None,
    },
    {
        'type': MonitorType.GPU,
        'enabled_preference_key': PreferenceKeys.GPU_MONITOR_ENABLED,
        'monitor_class': GpuMonitorWidget,
        'preference_toggle_label': 'GPU (experimental)',
        'preference_toggle_section_name': None,
    },
    {
        'type': MonitorType.Memory,
        'enabled_preference_key': PreferenceKeys.MEMORY_MONITOR_ENABLED,
        'monitor_class': MemoryMonitorWidget,
        'preference_toggle_label': 'Memory',
        'preference_toggle_section_name': None,
    },
    {
        'type': MonitorType.Downlink,
        'enabled_preference_key': PreferenceKeys.DOWNLINK_MONITOR_ENABLED,
        'monitor_class': DownlinkMonitorWidget,
        'preference_toggle_label': 'Downlink',
        'preference_toggle_section_name': 'Network',
    },
    {
        'type': MonitorType.Uplink,
        'enabled_preference_key': PreferenceKeys.UPLINK_MONITOR_ENABLED,
        'monitor_class': UplinkMonitorWidget,
        'preference_toggle_label': 'Uplink',
        'preference_toggle_section_name': 'Network',
    },
    {
        'type': MonitorType.Home_usage,
        'enabled_preference_key': PreferenceKeys.HOME_USAGE_MONITOR_ENABLED,
        'monitor_class': HomeUsageMonitorWidget,
        'preference_toggle_label': 'Home folder usage',
        'preference_toggle_section_name': 'Disk usage',
    },
    {
        'type': MonitorType.Root_usage,
        'enabled_preference_key': PreferenceKeys.ROOT_USAGE_MONITOR_ENABLED,
        'monitor_class': RootUsageMonitorWidget,
        'preference_toggle_label': 'Root folder usage',
        'preference_toggle_section_name': 'Disk usage',
    },
]


def get_monitor_descriptors_grouped_by_preference_toggle_section():
    grouped_descriptors = {
        "toplevel": list(),
        "section": defaultdict(list)
    }

    for descriptor in monitor_descriptor_list:
        if descriptor["preference_toggle_section_name"] is None:
            grouped_descriptors["toplevel"].append(descriptor)
        else:
            grouped_descriptors["section"][descriptor["preference_toggle_section_name"]].append(descriptor)

    return grouped_descriptors
