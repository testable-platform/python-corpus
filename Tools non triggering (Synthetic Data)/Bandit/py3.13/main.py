"""saltworks evaporation pans: minimal program, py3.13."""
from typing import NamedTuple


class SaltworksEvaporationPansReading313(NamedTuple):
    """One reading of the saltworks evaporation pans."""

    carried: int
    total: int

    def line(self) -> str:
        """Return both figures as a line of text."""
        return f"saltworks evaporation pans: {self.total} of {self.carried}"


if __name__ == "__main__":
    print(SaltworksEvaporationPansReading313(37, 33).line())
