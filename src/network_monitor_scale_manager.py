from .event_broker import EventBroker
from . import events


class NetworkMonitorScaleManager:
    @classmethod
    def initialize(self):
        self._current_value = 0
        self._current_downlink_value = 0
        self._current_uplink_value = 0

        EventBroker.subscribe(events.DOWNLINK_NETWORK_MONITOR_NEW_REFERENCE_VALUE_PROPOSAL, self._new_downlink_monitor_value)
        EventBroker.subscribe(events.UPLINK_NETWORK_MONITOR_NEW_REFERENCE_VALUE_PROPOSAL, self._new_uplink_monitor_value)

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
            EventBroker.notify(events.NETWORK_MONITOR_NEW_REFERENCE_VALUE, self._current_value)
