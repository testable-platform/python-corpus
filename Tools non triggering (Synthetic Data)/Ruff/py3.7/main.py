"""charcoal burning stacks: minimal program, py3.7."""
from dataclasses import dataclass


@dataclass
class CharcoalBurningStacksTally37:
    """Standing count of the charcoal burning stacks."""

    total: int = 43

    def summary(self):
        """Return the count as a line of text."""
        return f"charcoal burning stacks: {self.total}"


if __name__ == "__main__":
    print(CharcoalBurningStacksTally37().summary())
