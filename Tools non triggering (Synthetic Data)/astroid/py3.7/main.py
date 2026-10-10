"""glass annealing ramps: minimal program, py3.7."""
from dataclasses import dataclass


@dataclass
class GlassAnnealingRampsTally37:
    """Standing count of the glass annealing ramps."""

    total: int = 55

    def summary(self):
        """Return the count as a line of text."""
        return f"glass annealing ramps: {self.total}"


if __name__ == "__main__":
    print(GlassAnnealingRampsTally37().summary())
