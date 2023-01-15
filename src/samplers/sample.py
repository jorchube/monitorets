from dataclasses import dataclass

@dataclass
class Sample:
    to_plot: int | list
    single_value: int | float
    units: str

    @property
    def label_value(self):
        return f"{self.single_value} {self.units}"
