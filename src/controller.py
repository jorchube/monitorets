from gi.repository import GObject
import traceback
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
        EventBroker.subscribe(events.MONITOR_ENABLED, self._handle_on_monitor_enabled)
        EventBroker.subscribe(events.MONITOR_DISABLED, self._handle_on_monitor_disabled)

        self._available_monitors = self._build_available_monitors_dict()
        self._enabled_monitors = dict()

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
    def _handle_on_monitor_enabled(self, type):
        GObject.idle_add(self._on_monitor_enabled, type)

    @classmethod
    def _handle_on_monitor_disabled(self, type):
        GObject.idle_add(self._on_monitor_disabled, type)

    @classmethod
    def _on_monitor_enabled(self, type):
        try:
            self._enable_monitor(type)
        except Exception as e:
            print(f"Exception: {e}")
            traceback.print_exc()

    @classmethod
    def _enable_monitor(self, type):
        if self._enabled_monitors.get(type) is not None:
            print(f"[Warning] {type} monitor is already enabled")
            return

        monitor = self._available_monitors[type]()
        self._enabled_monitors[type] = monitor
        monitor.start()
        WindowLayoutManager.add_monitor(monitor)

    @classmethod
    def _on_monitor_disabled(self, type):
        self._disable_monitor(type)

    @classmethod
    def _disable_monitor(self, type):
        monitor = self._enabled_monitors.get(type)
        if monitor is None:
            print(f"[Warning] {type} monitor is already disabled")
            return

        self._enabled_monitors[type] = None
        WindowLayoutManager.remove_monitor(monitor)
        monitor.stop()

    @classmethod
    def _build_available_monitors_dict(self):
        monitors_dict = {}
        for descriptor in monitor_descriptor_list:
            monitors_dict[descriptor["type"]] = descriptor["monitor_class"]

        return monitors_dict
