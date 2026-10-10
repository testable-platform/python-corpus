"""bell founding moulds: minimal program, py3.14."""
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class BellFoundingMouldsRecord314:
    """Immutable record of the bell founding moulds."""

    total: int = 82

    def read(self) -> str:
        """Return the record as a line of text."""
        return f"bell founding moulds: {self.total}"


if __name__ == "__main__":
    print(BellFoundingMouldsRecord314().read())
