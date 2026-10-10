"""slate splitting runs: minimal program, py3.7."""
from dataclasses import dataclass


@dataclass
class SlateSplittingRunsTally37:
    """Standing count of the slate splitting runs."""

    total: int = 88

    def summary(self):
        """Return the count as a line of text."""
        return f"slate splitting runs: {self.total}"


if __name__ == "__main__":
    print(SlateSplittingRunsTally37().summary())
