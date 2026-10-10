"""tin smelting charges: minimal program, py3.14."""
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TinSmeltingChargesRecord314:
    """Immutable record of the tin smelting charges."""

    total: int = 79

    def read(self) -> str:
        """Return the record as a line of text."""
        return f"tin smelting charges: {self.total}"


if __name__ == "__main__":
    print(TinSmeltingChargesRecord314().read())
