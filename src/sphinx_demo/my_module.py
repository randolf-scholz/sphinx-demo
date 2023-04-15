"""Example Module."""

__all__ = ["MyClass"]


CONST: int = 42
"""Example constant."""


class MyClass:
    """Example class."""

    x: float
    """Example attribute."""
    y: float
    """Example attribute."""

    def __init__(self, x: float, y: float) -> None:
        """Initialize the class."""
        self.x = x
        self.y = y

    def compute_difference(self) -> float:
        """Compute the difference $x-y$."""
        return self.x - self.y


def bar(a: int) -> int:
    """Doubles the input $y=2x$."""
    return 2 * a
