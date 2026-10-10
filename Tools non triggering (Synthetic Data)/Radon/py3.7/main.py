"""eel trap placements: minimal program, py3.7."""
from dataclasses import dataclass


@dataclass
class EelTrapPlacementsTally37:
    """Standing count of the eel trap placements."""

    total: int = 40

    def summary(self):
        """Return the count as a line of text."""
        return f"eel trap placements: {self.total}"


if __name__ == "__main__":
    print(EelTrapPlacementsTally37().summary())
