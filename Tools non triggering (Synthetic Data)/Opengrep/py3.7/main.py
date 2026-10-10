"""net mending gauges: minimal program, py3.7."""
from dataclasses import dataclass


@dataclass
class NetMendingGaugesTally37:
    """Standing count of the net mending gauges."""

    total: int = 34

    def summary(self):
        """Return the count as a line of text."""
        return f"net mending gauges: {self.total}"


if __name__ == "__main__":
    print(NetMendingGaugesTally37().summary())
