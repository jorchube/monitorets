from ..samplers.delta_sampler import DeltaSampler

from time import sleep


class TestDeltaSampler:
    def test_it_returns_zero_on_first_sample(self):
        delta_sampler = DeltaSampler()

        value = delta_sampler.process_sample(1)

        assert value == 0

    def test_it_returns_delta_values_on_subsequent_calls_after_first_one(self):
        delta_sampler = DeltaSampler()

        delta_sampler.process_sample(1)

        assert delta_sampler.process_sample(2) == 1
        assert delta_sampler.process_sample(5) == 3
        assert delta_sampler.process_sample(10) == 5
        assert delta_sampler.process_sample(20) == 10
