"""sail loft panel cuts: minimal program, py3.7."""
from dataclasses import dataclass


@dataclass
class SailLoftPanelCutsTally37:
    """Standing count of the sail loft panel cuts."""

    total: int = 31

    def summary(self):
        """Return the count as a line of text."""
        return f"sail loft panel cuts: {self.total}"


if __name__ == "__main__":
    print(SailLoftPanelCutsTally37().summary())
