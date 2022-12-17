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
from .translatable_strings import (
    preference_toggle_label,
    preference_toggle_section_name
)


monitor_descriptor_list = [
    {
        'type': MonitorType.CPU,
        'enabled_preference_key': PreferenceKeys.CPU_MONITOR_ENABLED,
        'monitor_class': CpuMonitorWidget,
        'preference_toggle_label': preference_toggle_label.CPU,
        'preference_toggle_section_name': preference_toggle_section_name.CPU,
    },
    {
        'type': MonitorType.GPU,
        'enabled_preference_key': PreferenceKeys.GPU_MONITOR_ENABLED,
        'monitor_class': GpuMonitorWidget,
        'preference_toggle_label': preference_toggle_label.GPU,
        'preference_toggle_section_name': preference_toggle_section_name.GPU,
    },
    {
        'type': MonitorType.Memory,
        'enabled_preference_key': PreferenceKeys.MEMORY_MONITOR_ENABLED,
        'monitor_class': MemoryMonitorWidget,
        'preference_toggle_label': preference_toggle_label.MEMORY,
        'preference_toggle_section_name': preference_toggle_section_name.MEMORY,
    },
    {
        'type': MonitorType.Downlink,
        'enabled_preference_key': PreferenceKeys.DOWNLINK_MONITOR_ENABLED,
        'monitor_class': DownlinkMonitorWidget,
        'preference_toggle_label': preference_toggle_label.DOWNLINK,
        'preference_toggle_section_name': preference_toggle_section_name.NETWORK,
    },
    {
        'type': MonitorType.Uplink,
        'enabled_preference_key': PreferenceKeys.UPLINK_MONITOR_ENABLED,
        'monitor_class': UplinkMonitorWidget,
        'preference_toggle_label': preference_toggle_label.UPLINK,
        'preference_toggle_section_name': preference_toggle_section_name.NETWORK,
    },
    {
        'type': MonitorType.Home_usage,
        'enabled_preference_key': PreferenceKeys.HOME_USAGE_MONITOR_ENABLED,
        'monitor_class': HomeUsageMonitorWidget,
        'preference_toggle_label': preference_toggle_label.HOME_FOLDER_USAGE,
        'preference_toggle_section_name': preference_toggle_section_name.DISK_USAGE,
    },
    {
        'type': MonitorType.Root_usage,
        'enabled_preference_key': PreferenceKeys.ROOT_USAGE_MONITOR_ENABLED,
        'monitor_class': RootUsageMonitorWidget,
        'preference_toggle_label': preference_toggle_label.ROOT_FOLDER_USAGE,
        'preference_toggle_section_name': preference_toggle_section_name.DISK_USAGE,
    },
]


def get_monitor_descriptors_grouped_by_preference_toggle_section():
    grouped_descriptors = {
        "toplevel": list(),
        "section": defaultdict(list)
    }

    grouped_descriptors = defaultdict(list)

    for descriptor in monitor_descriptor_list:
        grouped_descriptors[descriptor["preference_toggle_section_name"]].append(descriptor)

    return grouped_descriptors


def register_monitor_descriptor(new_descriptor):
    monitor_descriptor_list.append(new_descriptor)
