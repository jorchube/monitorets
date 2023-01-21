from concurrent.futures import ThreadPoolExecutor


class EventBroker:
    _NUMBER_OF_WORKERS = 4

    _subscriptions = dict()
    _thread_pool_executor = None

    @classmethod
    def subscribe(cls, event, subscription):
        if event not in cls._subscriptions:
            cls._subscriptions[event] = set()

        cls._subscriptions[event].add(subscription)

    @classmethod
    def notify(cls, event, *args, **kwargs):
        print(f"[Event] {event} {args} {kwargs}")
        if event not in cls._subscriptions:
            return

        for subscription in cls._subscriptions[event]:
            cls._execute_in_thread(subscription, *args, **kwargs)

    @classmethod
    def initialize(cls):
        cls._thread_pool_executor = ThreadPoolExecutor(
            max_workers=cls._NUMBER_OF_WORKERS
        )

    @classmethod
    def _execute_in_thread(cls, call, *args, **kwargs):
        cls._thread_pool_executor.submit(call, *args, **kwargs)
