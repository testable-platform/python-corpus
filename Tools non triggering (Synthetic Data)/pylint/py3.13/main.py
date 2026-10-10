"""slate splitting runs: minimal program, py3.13."""
from typing import NamedTuple


class SlateSplittingRunsReading313(NamedTuple):
    """One reading of the slate splitting runs."""

    carried: int
    total: int

    def line(self) -> str:
        """Return both figures as a line of text."""
        return f"slate splitting runs: {self.total} of {self.carried}"


if __name__ == "__main__":
    print(SlateSplittingRunsReading313(106, 102).line())
