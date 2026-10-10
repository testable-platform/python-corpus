"""eel trap placements: minimal program, py3.13."""
from typing import NamedTuple


class EelTrapPlacementsReading313(NamedTuple):
    """One reading of the eel trap placements."""

    carried: int
    total: int

    def line(self) -> str:
        """Return both figures as a line of text."""
        return f"eel trap placements: {self.total} of {self.carried}"


if __name__ == "__main__":
    print(EelTrapPlacementsReading313(58, 54).line())
