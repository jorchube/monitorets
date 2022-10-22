from . import events
from .event_broker import EventBroker
from .preferences import Preferences
from .monitor_type import MonitorType
from .theming import Theming


class Controller:
    _CPU_MONITOR_ENABLED_KEY = "cpu_monitor.enabled"
    _GPU_MONITOR_ENABLED_KEY = "gpu_monitor.enabled"
    _MEMORY_MONITOR_ENABLED_KEY = "memory_monitor.enabled"

    @classmethod
    def initialize(self, application):
        self._application = application

        EventBroker.initialize()
        Preferences.load()
        Theming.initialize()

        EventBroker.subscribe(events.PREFERENCES_CHANGED, self._on_preference_changed)

    @classmethod
    def show_monitors(self):
        if Preferences.get("cpu_monitor.enabled"):
            EventBroker.notify(events.MONITOR_ENABLED, MonitorType.CPU)

        if Preferences.get("gpu_monitor.enabled"):
            EventBroker.notify(events.MONITOR_ENABLED, MonitorType.GPU)

        if Preferences.get("memory_monitor.enabled"):
            EventBroker.notify(events.MONITOR_ENABLED, MonitorType.Memory)

    @classmethod
    def _on_preference_changed(self, preference_key, value):
        if preference_key == self._CPU_MONITOR_ENABLED_KEY:
            self._on_monitor_enabled_changed(MonitorType.CPU, value)

        if preference_key == self._GPU_MONITOR_ENABLED_KEY:
            self._on_monitor_enabled_changed(MonitorType.GPU, value)

        if preference_key == self._MEMORY_MONITOR_ENABLED_KEY:
            self._on_monitor_enabled_changed(MonitorType.Memory, value)

    @classmethod
    def _on_monitor_enabled_changed(self, monitor_type, enabled):
        if enabled:
            event = events.MONITOR_ENABLED
        else:
            event = events.MONITOR_DISABLED

        EventBroker.notify(event, monitor_type)
