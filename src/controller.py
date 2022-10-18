from gi.repository import GObject

from . import events
from .event_broker import EventBroker
from .preferences import Preferences
from .monitor_windows.cpu_monitor_window import CPUMonitorWindow
from .monitor_windows.gpu_monitor_window import GPUMonitorWindow
from .monitor_windows.memory_monitor_window import MemoryMonitorWindow
from .monitor_type import MonitorType
from .theming import Theming


_monitor_type_to_window_map = {
    MonitorType.CPU: CPUMonitorWindow,
    MonitorType.GPU: GPUMonitorWindow,
    MonitorType.Memory: MemoryMonitorWindow,
}


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
            CPUMonitorWindow(application=self._application).present()

        if Preferences.get("gpu_monitor.enabled"):
            GPUMonitorWindow(application=self._application).present()

        if Preferences.get("memory_monitor.enabled"):
            MemoryMonitorWindow(application=self._application).present()

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
            GObject.idle_add(self._create_monitor_window, monitor_type)

        if not enabled:
            GObject.idle_add(self._close_monitor_windows, monitor_type)

    @classmethod
    def _create_monitor_window(self, monitor_type):
        if monitor_type in self._get_active_monitor_types():
            return
        _monitor_type_to_window_map[monitor_type](application=self._application).present()

    @classmethod
    def _get_active_monitor_types(self):
        windows = self._application.get_windows()
        return [window.monitor_type for window in windows]

    @classmethod
    def _close_monitor_windows(self, type):
        for monitor_window in self._application.get_windows():
            if monitor_window.monitor_type == type:
                monitor_window.close()
