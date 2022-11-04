from .monitor_type import MonitorType


monitor_descriptor_list = [
    {
        'type': MonitorType.CPU,
        'enabled_preference_key': "cpu_monitor.enabled",
    },
    {
        'type': MonitorType.GPU,
        'enabled_preference_key': "gpu_monitor.enabled",
    },
    {
        'type': MonitorType.Memory,
        'enabled_preference_key': "memory_monitor.enabled",
    },
]
