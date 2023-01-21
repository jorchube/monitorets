from .event_broker import EventBroker
from . import events
from .monitor_type import MonitorType
from .preferences import Preferences
from .preference_keys import PreferenceKeys


class NetworkMonitorScaleManager:
    @classmethod
    def initialize(self):
        self._current_value = 0
        self._current_downlink_value = 0
        self._current_uplink_value = 0

        EventBroker.subscribe(events.MONITOR_ENABLED, self._on_monitor_enabled)
        EventBroker.subscribe(events.MONITOR_DISABLED, self._on_monitor_disabled)
        EventBroker.subscribe(
            events.DOWNLINK_NETWORK_MONITOR_NEW_REFERENCE_VALUE_PROPOSAL,
            self._new_downlink_monitor_value,
        )
        EventBroker.subscribe(
            events.UPLINK_NETWORK_MONITOR_NEW_REFERENCE_VALUE_PROPOSAL,
            self._new_uplink_monitor_value,
        )

    @classmethod
    def _new_downlink_monitor_value(self, value):
        self._current_downlink_value = value
        self._new_value_received()

    @classmethod
    def _new_uplink_monitor_value(self, value):
        self._current_uplink_value = value
        self._new_value_received()

    @classmethod
    def _new_value_received(self):
        candidate_value = max(self._current_downlink_value, self._current_uplink_value)

        if candidate_value != self._current_value:
            self._current_value = candidate_value
            EventBroker.notify(
                events.NETWORK_MONITOR_NEW_REFERENCE_VALUE, self._current_value
            )

    @classmethod
    def _on_monitor_enabled(self, monitor):
        if monitor in [MonitorType.Uplink, MonitorType.Downlink]:
            self._refresh_use_shared_scaling_preference_value()

    @classmethod
    def _on_monitor_disabled(self, monitor):
        if monitor in [MonitorType.Uplink, MonitorType.Downlink]:
            self._refresh_use_shared_scaling_preference_value()

    @classmethod
    def _refresh_use_shared_scaling_preference_value(self):
        if (
            Preferences.get(PreferenceKeys.UPLINK_MONITOR_ENABLED) is False
            or Preferences.get(PreferenceKeys.DOWNLINK_MONITOR_ENABLED) is False
        ):
            Preferences.set(
                PreferenceKeys.UNIFIED_SCALE_FOR_NETWORK_MONITORS_ENABLED, False
            )
            return

        Preferences.set(PreferenceKeys.UNIFIED_SCALE_FOR_NETWORK_MONITORS_ENABLED, True)
