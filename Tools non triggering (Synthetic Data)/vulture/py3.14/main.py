"""candle dipping rounds: minimal program, py3.14."""
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CandleDippingRoundsRecord314:
    """Immutable record of the candle dipping rounds."""

    total: int = 121

    def read(self) -> str:
        """Return the record as a line of text."""
        return f"candle dipping rounds: {self.total}"


if __name__ == "__main__":
    print(CandleDippingRoundsRecord314().read())
