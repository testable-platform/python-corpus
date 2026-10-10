"""bell founding moulds: minimal program, py3.13."""
from typing import NamedTuple


class BellFoundingMouldsReading313(NamedTuple):
    """One reading of the bell founding moulds."""

    carried: int
    total: int

    def line(self) -> str:
        """Return both figures as a line of text."""
        return f"bell founding moulds: {self.total} of {self.carried}"


if __name__ == "__main__":
    print(BellFoundingMouldsReading313(79, 75).line())
