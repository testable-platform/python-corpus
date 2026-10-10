"""ice house packings: minimal program, py3.14."""
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class IceHousePackingsRecord314:
    """Immutable record of the ice house packings."""

    total: int = 103

    def read(self) -> str:
        """Return the record as a line of text."""
        return f"ice house packings: {self.total}"


if __name__ == "__main__":
    print(IceHousePackingsRecord314().read())
