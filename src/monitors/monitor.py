class Monitor:
    _MAX_NUMBER_OF_VALUES_STORED = 55

    def __init__(self, sampler):
        self._sampler = sampler
        self._sampler.install_new_sample_callback(self._new_sample)
        self._new_values_callback = None
        self._graph_values = []

    def start(self):
        self._sampler.start()

    def stop(self):
        self._sampler.stop()

    def install_new_values_callback(self, cb):
        self._new_values_callback = cb

    def _new_sample(self, sample):
        self._last_readable_value = sample.label_value
        self._graph_values.insert(0, sample.to_plot)
        if self._new_values_callback:
            self._report_values()

        if self._has_reached_max_values_stored():
            self._free_old_values()

    def _report_values(self):
        self._new_values_callback(self._graph_values, self._last_readable_value)

    def _has_reached_max_values_stored(self):
        return len(self._graph_values) > self._MAX_NUMBER_OF_VALUES_STORED

    def _free_old_values(self):
        self._graph_values = self._graph_values[:self._MAX_NUMBER_OF_VALUES_STORED]
