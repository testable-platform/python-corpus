"""hop kiln loads: minimal program, py3.13."""
from typing import NamedTuple


class HopKilnLoadsReading313(NamedTuple):
    """One reading of the hop kiln loads."""

    carried: int
    total: int

    def line(self) -> str:
        """Return both figures as a line of text."""
        return f"hop kiln loads: {self.total} of {self.carried}"


if __name__ == "__main__":
    print(HopKilnLoadsReading313(91, 87).line())
