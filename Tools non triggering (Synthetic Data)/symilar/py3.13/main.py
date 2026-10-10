"""marl digging pits: minimal program, py3.13."""
from typing import NamedTuple


class MarlDiggingPitsReading313(NamedTuple):
    """One reading of the marl digging pits."""

    carried: int
    total: int

    def line(self) -> str:
        """Return both figures as a line of text."""
        return f"marl digging pits: {self.total} of {self.carried}"


if __name__ == "__main__":
    print(MarlDiggingPitsReading313(109, 105).line())
