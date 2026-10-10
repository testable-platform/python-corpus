"""marl digging pits: minimal program, py3.14."""
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class MarlDiggingPitsRecord314:
    """Immutable record of the marl digging pits."""

    total: int = 112

    def read(self) -> str:
        """Return the record as a line of text."""
        return f"marl digging pits: {self.total}"


if __name__ == "__main__":
    print(MarlDiggingPitsRecord314().read())
