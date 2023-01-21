class GiB:
    value = 1024 * 1024 * 1024
    unit = "GiB"


class MiB:
    value = 1024 * 1024
    unit = "MiB"


class KiB:
    value = 1024
    unit = "KiB"


class Byte:
    value = 1
    unit = "B"


def convert(value, from_units, to_units):
    return value * (from_units.value / to_units.value)
