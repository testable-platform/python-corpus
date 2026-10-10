"""saltworks evaporation pans: minimal program, py3.14."""
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SaltworksEvaporationPansRecord314:
    """Immutable record of the saltworks evaporation pans."""

    total: int = 40

    def read(self) -> str:
        """Return the record as a line of text."""
        return f"saltworks evaporation pans: {self.total}"


if __name__ == "__main__":
    print(SaltworksEvaporationPansRecord314().read())
