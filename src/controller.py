from . import events
from .event_broker import EventBroker
from .preferences import Preferences
from .monitor_type import MonitorType
from .theming import Theming
from .monitor_descriptors import monitor_descriptor_list


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
        for descriptor in monitor_descriptor_list:
            if Preferences.get(descriptor["enabled_preference_key"]):
                EventBroker.notify(events.MONITOR_ENABLED, descriptor["type"])

    @classmethod
    def _on_preference_changed(self, preference_key, value):
        for descriptor in monitor_descriptor_list:
            if preference_key == descriptor["enabled_preference_key"]:
                self._on_monitor_enabled_changed(descriptor["type"], value)
                return

    @classmethod
    def _on_monitor_enabled_changed(self, monitor_type, enabled):
        if enabled:
            event = events.MONITOR_ENABLED
        else:
            event = events.MONITOR_DISABLED

        EventBroker.notify(event, monitor_type)
