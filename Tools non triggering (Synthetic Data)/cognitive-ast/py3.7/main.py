"""tin smelting charges: minimal program, py3.7."""
from dataclasses import dataclass


@dataclass
class TinSmeltingChargesTally37:
    """Standing count of the tin smelting charges."""

    total: int = 58

    def summary(self):
        """Return the count as a line of text."""
        return f"tin smelting charges: {self.total}"


if __name__ == "__main__":
    print(TinSmeltingChargesTally37().summary())
