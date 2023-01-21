import pytest
from unittest.mock import Mock, call
from ..event_broker import EventBroker
from .conftest import EventWaiter


class TestEventBroker:
    @pytest.fixture
    def mock_subscription(self):
        return Mock()

    @pytest.fixture
    def mock_subscription_2(self):
        return Mock()

    def test_it_notifies_event_to_a_subscription(
        self, mock_subscription, mock_subscription_2
    ):
        waiter = EventWaiter("some event")

        EventBroker.initialize()
        EventBroker.subscribe("some event", mock_subscription)
        EventBroker.subscribe("a different event", mock_subscription_2)

        EventBroker.notify("some event")

        assert waiter.wait_for_event()

        mock_subscription.assert_called_once()

    def test_it_notifies_event_to_many_subscriptions(
        self, mock_subscription, mock_subscription_2
    ):
        waiter = EventWaiter("another event")

        EventBroker.initialize()
        EventBroker.subscribe("another event", mock_subscription)
        EventBroker.subscribe("another event", mock_subscription_2)

        EventBroker.notify("another event")

        assert waiter.wait_for_event()

        mock_subscription.assert_called_once()
        mock_subscription_2.assert_called_once()

    def test_it_notifies_many_events_to_a_subscription(self, mock_subscription):
        waiter1 = EventWaiter("some event")
        waiter2 = EventWaiter("a different event")

        EventBroker.initialize()
        EventBroker.subscribe("some event", mock_subscription)
        EventBroker.subscribe("a different event", mock_subscription)

        EventBroker.notify("some event")
        EventBroker.notify("a different event")

        assert waiter1.wait_for_event()
        assert waiter2.wait_for_event()

        mock_subscription.assert_has_calls(
            [
                call(),
                call(),
            ]
        )

    def test_it_notifies_event_with_extra_data_to_a_subscription(
        self, mock_subscription
    ):
        waiter = EventWaiter("some event")

        EventBroker.initialize()
        EventBroker.subscribe("some event", mock_subscription)

        EventBroker.notify(
            "some event",
            "positional arg 1",
            "positional arg 2",
            named_arg_1=1,
            named_arg_2=2,
        )

        assert waiter.wait_for_event()

        mock_subscription.assert_called_once_with(
            "positional arg 1", "positional arg 2", named_arg_1=1, named_arg_2=2
        )
