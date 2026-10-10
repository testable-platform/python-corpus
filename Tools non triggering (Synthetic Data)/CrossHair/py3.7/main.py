"""rope walk strand counts: minimal program, py3.7."""
from dataclasses import dataclass


@dataclass
class RopeWalkStrandCountsTally37:
    """Standing count of the rope walk strand counts."""

    total: int = 28

    def summary(self):
        """Return the count as a line of text."""
        return f"rope walk strand counts: {self.total}"


if __name__ == "__main__":
    print(RopeWalkStrandCountsTally37().summary())
