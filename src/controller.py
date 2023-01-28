from . import events
from .event_broker import EventBroker
from .preferences import Preferences
from .theming import Theming
from .monitor_descriptors import monitor_descriptor_list
from .network_monitor_scale_manager import NetworkMonitorScaleManager
from .ui.window_layout_manager import WindowLayoutManager


class Controller:
    @classmethod
    def initialize(self, application):
        self._application = application

        EventBroker.initialize()
        Preferences.initialize()
        Preferences.load()
        Theming.initialize()
        NetworkMonitorScaleManager.initialize()
        WindowLayoutManager.initialize()

        EventBroker.subscribe(events.PREFERENCES_CHANGED, self._on_preference_changed)

        # self._available_monitors = self._build_available_monitors_dict()
        # self._enabled_monitors = dict()

    @classmethod
    def show_monitors(self):
        for descriptor in monitor_descriptor_list:
            if Preferences.get(descriptor["enabled_preference_key"]):
                EventBroker.notify(events.MONITOR_ENABLED, descriptor["type"])

    @classmethod
    def _restart_monitors(self):
        for descriptor in monitor_descriptor_list:
            EventBroker.notify(events.MONITOR_DISABLED, descriptor["type"])

        self.show_monitors()

    @classmethod
    def _on_preference_changed(self, preference_key, value):
        if preference_key == "general.smooth_graph":
            self._restart_monitors()
            return

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

    @classmethod
    def _build_available_monitors_dict(self):
        monitors_dict = {}
        for descriptor in monitor_descriptor_list:
            monitors_dict[descriptor["type"]] = descriptor["monitor_class"]

        return monitors_dict
