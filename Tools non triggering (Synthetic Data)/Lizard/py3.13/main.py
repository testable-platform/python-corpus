"""sail loft panel cuts: minimal program, py3.13."""
from typing import NamedTuple


class SailLoftPanelCutsReading313(NamedTuple):
    """One reading of the sail loft panel cuts."""

    carried: int
    total: int

    def line(self) -> str:
        """Return both figures as a line of text."""
        return f"sail loft panel cuts: {self.total} of {self.carried}"


if __name__ == "__main__":
    print(SailLoftPanelCutsReading313(49, 45).line())
