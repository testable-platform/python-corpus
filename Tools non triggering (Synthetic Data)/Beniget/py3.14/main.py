"""peat cutting allocations: minimal program, py3.14."""
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PeatCuttingAllocationsRecord314:
    """Immutable record of the peat cutting allocations."""

    total: int = 43

    def read(self) -> str:
        """Return the record as a line of text."""
        return f"peat cutting allocations: {self.total}"


if __name__ == "__main__":
    print(PeatCuttingAllocationsRecord314().read())
