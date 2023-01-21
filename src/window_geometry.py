from dataclasses import dataclass, asdict

@dataclass
class WindowGeometry:
    width: int
    height: int

    def as_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(self, a_dict):
        return WindowGeometry(**a_dict)
