import psutil

from .. import units
from .delta_sampler import DeltaSampler
from .sampler import Sampler
from .sample import Sample


class UplinkSampler(Sampler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._delta_sampler = DeltaSampler()

    def _get_sample(self):
        per_nic_counters = psutil.net_io_counters(pernic=True)

        counter = 0
        for key, value in per_nic_counters.items():
            if key != 'lo':
                counter += value.bytes_sent

        value = int(self._delta_sampler.process_sample(counter))
        single_value, unit = self._get_single_value_and_unit(value)

        sample = Sample(
            to_plot=value,
            single_value=round(single_value),
            units=f"{unit}/s"
        )

        return sample

    def _get_single_value_and_unit(self, value):
        _units = units.Byte
        if value > units.KiB.value:
            _units = units.KiB
        if value > units.MiB.value:
            _units = units.MiB
        if value > units.GiB.value:
            _units = units.GiB

        return units.convert(value, units.Byte, _units), _units.unit
