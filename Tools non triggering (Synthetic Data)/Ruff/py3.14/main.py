"""charcoal burning stacks: minimal program, py3.14."""
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CharcoalBurningStacksRecord314:
    """Immutable record of the charcoal burning stacks."""

    total: int = 64

    def read(self) -> str:
        """Return the record as a line of text."""
        return f"charcoal burning stacks: {self.total}"


if __name__ == "__main__":
    print(CharcoalBurningStacksRecord314().read())
