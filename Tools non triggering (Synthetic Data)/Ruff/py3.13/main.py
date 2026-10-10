"""charcoal burning stacks: minimal program, py3.13."""
from typing import NamedTuple


class CharcoalBurningStacksReading313(NamedTuple):
    """One reading of the charcoal burning stacks."""

    carried: int
    total: int

    def line(self) -> str:
        """Return both figures as a line of text."""
        return f"charcoal burning stacks: {self.total} of {self.carried}"


if __name__ == "__main__":
    print(CharcoalBurningStacksReading313(61, 57).line())
