from gi.repository import GObject

from . import events
from .event_broker import EventBroker
from .preferences import Preferences
from .monitor_windows.cpu_monitor_window import CPUMonitorWindow
from .monitor_windows.gpu_monitor_window import GPUMonitorWindow
from .monitor_windows.memory_monitor_window import MemoryMonitorWindow
from .monitor_type import MonitorType


class Controller:
    @classmethod
    def initialize(self, application):
        self._application = application

        EventBroker.initialize()
        Preferences.load()

        EventBroker.subscribe(events.MONITOR_ENABLED_CHANGED, self._on_monitor_enabled_changed)

    @classmethod
    def show_monitors(self):
        self._create_monitor_window(MonitorType.CPU)
        self._create_monitor_window(MonitorType.GPU)
        self._create_monitor_window(MonitorType.Memory)

    @classmethod
    def _on_monitor_enabled_changed(self, monitor_type, enabled):
        if enabled:
            GObject.idle_add(self._create_monitor_window, monitor_type)

        if not enabled:
            GObject.idle_add(self._close_monitor_windows, monitor_type)

    @classmethod
    def _create_monitor_window(self, monitor_type):
        if monitor_type == MonitorType.CPU:
            CPUMonitorWindow(application=self._application).present()
        if monitor_type == MonitorType.GPU:
            GPUMonitorWindow(application=self._application).present()
        if monitor_type == MonitorType.Memory:
            MemoryMonitorWindow(application=self._application).present()

    @classmethod
    def _close_monitor_windows(self, type):
        for monitor_window in self._application.get_windows():
            if monitor_window.monitor_type == type:
                monitor_window.close()
