"""peat cutting allocations: minimal program, py3.7."""
from dataclasses import dataclass


@dataclass
class PeatCuttingAllocationsTally37:
    """Standing count of the peat cutting allocations."""

    total: int = 22

    def summary(self):
        """Return the count as a line of text."""
        return f"peat cutting allocations: {self.total}"


if __name__ == "__main__":
    print(PeatCuttingAllocationsTally37().summary())
