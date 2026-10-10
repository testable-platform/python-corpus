"""glass annealing ramps: minimal program, py3.13."""
from typing import NamedTuple


class GlassAnnealingRampsReading313(NamedTuple):
    """One reading of the glass annealing ramps."""

    carried: int
    total: int

    def line(self) -> str:
        """Return both figures as a line of text."""
        return f"glass annealing ramps: {self.total} of {self.carried}"


if __name__ == "__main__":
    print(GlassAnnealingRampsReading313(73, 69).line())
