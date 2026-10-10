"""hop kiln loads: minimal program, py3.7."""
from dataclasses import dataclass


@dataclass
class HopKilnLoadsTally37:
    """Standing count of the hop kiln loads."""

    total: int = 73

    def summary(self):
        """Return the count as a line of text."""
        return f"hop kiln loads: {self.total}"


if __name__ == "__main__":
    print(HopKilnLoadsTally37().summary())
