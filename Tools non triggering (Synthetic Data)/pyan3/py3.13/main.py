"""ice house packings: minimal program, py3.13."""
from typing import NamedTuple


class IceHousePackingsReading313(NamedTuple):
    """One reading of the ice house packings."""

    carried: int
    total: int

    def line(self) -> str:
        """Return both figures as a line of text."""
        return f"ice house packings: {self.total} of {self.carried}"


if __name__ == "__main__":
    print(IceHousePackingsReading313(100, 96).line())
