"""ice house packings: minimal program, py3.7."""
from dataclasses import dataclass


@dataclass
class IceHousePackingsTally37:
    """Standing count of the ice house packings."""

    total: int = 82

    def summary(self):
        """Return the count as a line of text."""
        return f"ice house packings: {self.total}"


if __name__ == "__main__":
    print(IceHousePackingsTally37().summary())
