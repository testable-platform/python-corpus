"""tin smelting charges: minimal program, py3.13."""
from typing import NamedTuple


class TinSmeltingChargesReading313(NamedTuple):
    """One reading of the tin smelting charges."""

    carried: int
    total: int

    def line(self) -> str:
        """Return both figures as a line of text."""
        return f"tin smelting charges: {self.total} of {self.carried}"


if __name__ == "__main__":
    print(TinSmeltingChargesReading313(76, 72).line())
