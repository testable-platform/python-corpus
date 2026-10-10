"""candle dipping rounds: minimal program, py3.13."""
from typing import NamedTuple


class CandleDippingRoundsReading313(NamedTuple):
    """One reading of the candle dipping rounds."""

    carried: int
    total: int

    def line(self) -> str:
        """Return both figures as a line of text."""
        return f"candle dipping rounds: {self.total} of {self.carried}"


if __name__ == "__main__":
    print(CandleDippingRoundsReading313(118, 114).line())
