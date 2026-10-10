"""net mending gauges: minimal program, py3.13."""
from typing import NamedTuple


class NetMendingGaugesReading313(NamedTuple):
    """One reading of the net mending gauges."""

    carried: int
    total: int

    def line(self) -> str:
        """Return both figures as a line of text."""
        return f"net mending gauges: {self.total} of {self.carried}"


if __name__ == "__main__":
    print(NetMendingGaugesReading313(52, 48).line())
