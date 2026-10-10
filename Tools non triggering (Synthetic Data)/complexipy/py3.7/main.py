"""bell founding moulds: minimal program, py3.7."""
from dataclasses import dataclass


@dataclass
class BellFoundingMouldsTally37:
    """Standing count of the bell founding moulds."""

    total: int = 61

    def summary(self):
        """Return the count as a line of text."""
        return f"bell founding moulds: {self.total}"


if __name__ == "__main__":
    print(BellFoundingMouldsTally37().summary())
