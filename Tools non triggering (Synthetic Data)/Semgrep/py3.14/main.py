"""flax retting ponds: minimal program, py3.14."""
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FlaxRettingPondsRecord314:
    """Immutable record of the flax retting ponds."""

    total: int = 67

    def read(self) -> str:
        """Return the record as a line of text."""
        return f"flax retting ponds: {self.total}"


if __name__ == "__main__":
    print(FlaxRettingPondsRecord314().read())
