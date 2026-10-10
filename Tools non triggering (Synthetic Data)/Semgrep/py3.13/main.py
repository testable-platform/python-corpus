"""flax retting ponds: minimal program, py3.13."""
from typing import NamedTuple


class FlaxRettingPondsReading313(NamedTuple):
    """One reading of the flax retting ponds."""

    carried: int
    total: int

    def line(self) -> str:
        """Return both figures as a line of text."""
        return f"flax retting ponds: {self.total} of {self.carried}"


if __name__ == "__main__":
    print(FlaxRettingPondsReading313(64, 60).line())
