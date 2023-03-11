from .pressure_sampler import PressureSampler


class IOPressureSampler(PressureSampler):
    def __init__(self, *args, **kwargs):
        super().__init__(pressure_file_path="/proc/pressure/io", *args, **kwargs)
