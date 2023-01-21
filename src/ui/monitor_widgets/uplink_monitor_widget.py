from .monitor_widget import MonitorWidget
from ...monitors.uplink_monitor import UplinkMonitor
from ..relative_graph_area import RelativeGraphArea
from .. import colors
from ...translatable_strings import monitor_title
from ...monitor_type import MonitorType
from ...event_broker import EventBroker
from ... import events
from ...preferences import Preferences
from ...preference_keys import PreferenceKeys


class UplinkMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        self._type = MonitorType.Uplink
        self._title = monitor_title.UPLINK
        self._color = colors.RED
        self._monitor = UplinkMonitor()
        self._relative_graph_area = None
        self._use_unified_network_scale = Preferences.get(
            PreferenceKeys.UNIFIED_SCALE_FOR_NETWORK_MONITORS_ENABLED
        )

        EventBroker.subscribe(events.PREFERENCES_CHANGED, self._on_preference_changed)
        EventBroker.subscribe(
            events.NETWORK_MONITOR_NEW_REFERENCE_VALUE, self._set_new_reference_value
        )

        super().__init__(
            self._monitor, self._type, self._title, self._color, *args, **kwargs
        )

    def _graph_area_instance(self, color, redraw_freq_seconds, draw_smooth_graph):
        self._relative_graph_area = RelativeGraphArea(
            color,
            redraw_freq_seconds,
            draw_smooth_graph,
            new_reference_value_callback=self._new_reference_value,
        )
        return self._relative_graph_area

    def _new_reference_value(self, value):
        if self._use_unified_network_scale:
            EventBroker.notify(
                events.UPLINK_NETWORK_MONITOR_NEW_REFERENCE_VALUE_PROPOSAL, value
            )
        else:
            self._relative_graph_area.set_reference_value(value)

    def _set_new_reference_value(self, value):
        self._relative_graph_area.set_reference_value(value)

    def _on_preference_changed(self, key, value):
        if key == PreferenceKeys.UNIFIED_SCALE_FOR_NETWORK_MONITORS_ENABLED:
            self._use_unified_network_scale = value
            return

        super()._on_preference_changed(key, value)
