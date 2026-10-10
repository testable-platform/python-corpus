"""saltworks evaporation pans: minimal program, py3.7."""
from dataclasses import dataclass


@dataclass
class SaltworksEvaporationPansTally37:
    """Standing count of the saltworks evaporation pans."""

    total: int = 19

    def summary(self):
        """Return the count as a line of text."""
        return f"saltworks evaporation pans: {self.total}"


if __name__ == "__main__":
    print(SaltworksEvaporationPansTally37().summary())
