"""marl digging pits: minimal program, py3.7."""
from dataclasses import dataclass


@dataclass
class MarlDiggingPitsTally37:
    """Standing count of the marl digging pits."""

    total: int = 91

    def summary(self):
        """Return the count as a line of text."""
        return f"marl digging pits: {self.total}"


if __name__ == "__main__":
    print(MarlDiggingPitsTally37().summary())
