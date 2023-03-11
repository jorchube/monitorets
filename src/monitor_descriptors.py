from collections import defaultdict

from .monitor_type import MonitorType
from .preference_keys import PreferenceKeys
from .ui.monitor_widgets.cpu_monitor_widget import CpuMonitorWidget
from .ui.monitor_widgets.cpu_per_core_monitor_widget import CpuPerCoreMonitorWidget
from .ui.monitor_widgets.gpu_monitor_widget import GpuMonitorWidget
from .ui.monitor_widgets.memory_monitor_widget import MemoryMonitorWidget
from .ui.monitor_widgets.swap_monitor_widget import SwapMonitorWidget
from .ui.monitor_widgets.downlink_monitor_widget import DownlinkMonitorWidget
from .ui.monitor_widgets.uplink_monitor_widget import UplinkMonitorWidget
from .ui.monitor_widgets.home_usage_monitor_widget import HomeUsageMonitorWidget
from .ui.monitor_widgets.root_usage_monitor_widget import RootUsageMonitorWidget
from .ui.monitor_widgets.cpu_pressure_monitor_widget import CpuPressureMonitorWidget
from .ui.monitor_widgets.memory_pressure_monitor_widget import (
    MemoryPressureMonitorWidget,
)
from .ui.monitor_widgets.io_pressure_monitor_widget import IOPressureMonitorWidget
from .translatable_strings import (
    preference_toggle_label,
    preference_toggle_description,
    preference_toggle_section_name,
)


monitor_descriptor_list = [
    {
        "type": MonitorType.CPU,
        "enabled_preference_key": PreferenceKeys.CPU_MONITOR_ENABLED,
        "monitor_class": CpuMonitorWidget,
        "preference_toggle_label": preference_toggle_label.CPU,
        "preference_toggle_description": None,
        "preference_toggle_section_name": preference_toggle_section_name.CPU,
        "default_order": 1,
    },
    {
        "type": MonitorType.CPU_PER_CORE,
        "enabled_preference_key": PreferenceKeys.CPU_PER_CORE_MONITOR_ENABLED,
        "monitor_class": CpuPerCoreMonitorWidget,
        "preference_toggle_label": preference_toggle_label.CPU_PER_CORE,
        "preference_toggle_description": preference_toggle_description.CPU_PER_CORE,
        "preference_toggle_section_name": preference_toggle_section_name.CPU,
        "default_order": 2,
    },
    {
        "type": MonitorType.GPU,
        "enabled_preference_key": PreferenceKeys.GPU_MONITOR_ENABLED,
        "monitor_class": GpuMonitorWidget,
        "preference_toggle_label": preference_toggle_label.GPU,
        "preference_toggle_description": preference_toggle_description.GPU,
        "preference_toggle_section_name": preference_toggle_section_name.GPU,
        "default_order": 3,
    },
    {
        "type": MonitorType.Memory,
        "enabled_preference_key": PreferenceKeys.MEMORY_MONITOR_ENABLED,
        "monitor_class": MemoryMonitorWidget,
        "preference_toggle_label": preference_toggle_label.MEMORY,
        "preference_toggle_description": None,
        "preference_toggle_section_name": preference_toggle_section_name.MEMORY,
        "default_order": 4,
    },
    {
        "type": MonitorType.Swap,
        "enabled_preference_key": PreferenceKeys.SWAP_MONITOR_ENABLED,
        "monitor_class": SwapMonitorWidget,
        "preference_toggle_label": preference_toggle_label.SWAP,
        "preference_toggle_description": None,
        "preference_toggle_section_name": preference_toggle_section_name.MEMORY,
        "default_order": 5,
    },
    {
        "type": MonitorType.Downlink,
        "enabled_preference_key": PreferenceKeys.DOWNLINK_MONITOR_ENABLED,
        "monitor_class": DownlinkMonitorWidget,
        "preference_toggle_label": preference_toggle_label.DOWNLINK,
        "preference_toggle_description": None,
        "preference_toggle_section_name": preference_toggle_section_name.NETWORK,
        "default_order": 6,
    },
    {
        "type": MonitorType.Uplink,
        "enabled_preference_key": PreferenceKeys.UPLINK_MONITOR_ENABLED,
        "monitor_class": UplinkMonitorWidget,
        "preference_toggle_label": preference_toggle_label.UPLINK,
        "preference_toggle_description": None,
        "preference_toggle_section_name": preference_toggle_section_name.NETWORK,
        "default_order": 7,
    },
    {
        "type": MonitorType.Home_usage,
        "enabled_preference_key": PreferenceKeys.HOME_USAGE_MONITOR_ENABLED,
        "monitor_class": HomeUsageMonitorWidget,
        "preference_toggle_label": preference_toggle_label.HOME_FOLDER_USAGE,
        "preference_toggle_description": None,
        "preference_toggle_section_name": preference_toggle_section_name.DISK_USAGE,
        "default_order": 8,
    },
    {
        "type": MonitorType.Root_usage,
        "enabled_preference_key": PreferenceKeys.ROOT_USAGE_MONITOR_ENABLED,
        "monitor_class": RootUsageMonitorWidget,
        "preference_toggle_label": preference_toggle_label.ROOT_FOLDER_USAGE,
        "preference_toggle_description": None,
        "preference_toggle_section_name": preference_toggle_section_name.DISK_USAGE,
        "default_order": 9,
    },
    {
        "type": MonitorType.CPU_PRESSURE,
        "enabled_preference_key": PreferenceKeys.CPU_PRESSURE_MONITOR_ENABLED,
        "monitor_class": CpuPressureMonitorWidget,
        "preference_toggle_label": preference_toggle_label.CPU_PRESSURE,
        "preference_toggle_description": None,
        "preference_toggle_section_name": preference_toggle_section_name.PRESSURE,
        "default_order": 10,
    },
    {
        "type": MonitorType.MEMORY_PRESSURE,
        "enabled_preference_key": PreferenceKeys.MEMORY_PRESSURE_MONITOR_ENABLED,
        "monitor_class": MemoryPressureMonitorWidget,
        "preference_toggle_label": preference_toggle_label.MEMORY_PRESSURE,
        "preference_toggle_description": None,
        "preference_toggle_section_name": preference_toggle_section_name.PRESSURE,
        "default_order": 11,
    },
    {
        "type": MonitorType.IO_PRESSURE,
        "enabled_preference_key": PreferenceKeys.IO_PRESSURE_MONITOR_ENABLED,
        "monitor_class": IOPressureMonitorWidget,
        "preference_toggle_label": preference_toggle_label.IO_PRESSURE,
        "preference_toggle_description": None,
        "preference_toggle_section_name": preference_toggle_section_name.PRESSURE,
        "default_order": 12,
    },
]


def get_monitor_descriptors_grouped_by_preference_toggle_section():
    grouped_descriptors = {"toplevel": list(), "section": defaultdict(list)}

    grouped_descriptors = defaultdict(list)

    for descriptor in monitor_descriptor_list:
        grouped_descriptors[descriptor["preference_toggle_section_name"]].append(
            descriptor
        )

    return grouped_descriptors


def get_ordering_dict():
    ordering = dict()
    for descriptor in monitor_descriptor_list:
        ordering[descriptor["type"]] = descriptor["default_order"]

    return ordering


def register_monitor_descriptor(new_descriptor):
    new_descriptor["default_order"] = len(monitor_descriptor_list) + 1
    monitor_descriptor_list.append(new_descriptor)
