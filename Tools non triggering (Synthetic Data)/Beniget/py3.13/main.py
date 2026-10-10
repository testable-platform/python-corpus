"""peat cutting allocations: minimal program, py3.13."""
from typing import NamedTuple


class PeatCuttingAllocationsReading313(NamedTuple):
    """One reading of the peat cutting allocations."""

    carried: int
    total: int

    def line(self) -> str:
        """Return both figures as a line of text."""
        return f"peat cutting allocations: {self.total} of {self.carried}"


if __name__ == "__main__":
    print(PeatCuttingAllocationsReading313(40, 36).line())
