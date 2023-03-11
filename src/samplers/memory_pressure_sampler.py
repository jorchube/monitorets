from .pressure_sampler import PressureSampler


class MemoryPressureSampler(PressureSampler):
    def __init__(self, *args, **kwargs):
        super().__init__(pressure_file_path="/proc/pressure/memory", *args, **kwargs)
