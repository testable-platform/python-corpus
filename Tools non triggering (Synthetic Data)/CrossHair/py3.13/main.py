"""rope walk strand counts: minimal program, py3.13."""
from typing import NamedTuple


class RopeWalkStrandCountsReading313(NamedTuple):
    """One reading of the rope walk strand counts."""

    carried: int
    total: int

    def line(self) -> str:
        """Return both figures as a line of text."""
        return f"rope walk strand counts: {self.total} of {self.carried}"


if __name__ == "__main__":
    print(RopeWalkStrandCountsReading313(46, 42).line())
