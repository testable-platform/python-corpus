"""candle dipping rounds: minimal program, py3.7."""
from dataclasses import dataclass


@dataclass
class CandleDippingRoundsTally37:
    """Standing count of the candle dipping rounds."""

    total: int = 100

    def summary(self):
        """Return the count as a line of text."""
        return f"candle dipping rounds: {self.total}"


if __name__ == "__main__":
    print(CandleDippingRoundsTally37().summary())
