"""flax retting ponds: minimal program, py3.7."""
from dataclasses import dataclass


@dataclass
class FlaxRettingPondsTally37:
    """Standing count of the flax retting ponds."""

    total: int = 46

    def summary(self):
        """Return the count as a line of text."""
        return f"flax retting ponds: {self.total}"


if __name__ == "__main__":
    print(FlaxRettingPondsTally37().summary())
