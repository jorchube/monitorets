import time

from src.event_broker import EventBroker


class EventWaiter:
    _called = False

    def __init__(self, event):
        EventBroker.subscribe(event, self)

    def __call__(self, *args, **kwargs):
        self._called = True

    def wait_for_event(self, seconds=1):
        limit = time.time() + seconds

        while time.time() < limit and self._called is False:
            time.sleep(0.1)

        self._wait_for_other_subscribers()

        return self._called

    def _wait_for_other_subscribers(self):
        time.sleep(0.05)
