class Monitor:
    _MAX_NUMBER_OF_VALUES_STORED = 55

    def __init__(self, sampler):
        self._sampler = sampler
        self._sampler.install_new_sample_callback(self._new_sample)
        self._new_values_callback = None
        self._values = []

    def start(self):
        self._sampler.start()

    def stop(self):
        self._sampler.stop()

    def install_new_values_callback(self, cb):
        self._new_values_callback = cb

    def _new_sample(self, value):
        self._values.insert(0, value)
        if self._new_values_callback:
            self._new_values_callback(self._values)

        if self._has_reached_max_values_stored():
            self._free_old_values()

    def _has_reached_max_values_stored(self):
        return len(self._values) > self._MAX_NUMBER_OF_VALUES_STORED

    def _free_old_values(self):
        self._values = self._values[:self._MAX_NUMBER_OF_VALUES_STORED]
