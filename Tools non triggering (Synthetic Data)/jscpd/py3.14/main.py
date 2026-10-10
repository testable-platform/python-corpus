"""hop kiln loads: minimal program, py3.14."""
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HopKilnLoadsRecord314:
    """Immutable record of the hop kiln loads."""

    total: int = 94

    def read(self) -> str:
        """Return the record as a line of text."""
        return f"hop kiln loads: {self.total}"


if __name__ == "__main__":
    print(HopKilnLoadsRecord314().read())
