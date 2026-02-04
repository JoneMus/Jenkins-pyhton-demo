class SimpleMath:
    """Simple class for basic mathematical operations."""

    def _validate_input(self, a, b):
        """Validates that both inputs are numbers."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Input values must be numbers.")

    def add(self, a: int, b: int) -> int:
        """Returns the sum of two integers."""
        self._validate_input(a, b)
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """Returns the difference of two integers."""
        self._validate_input(a, b)
        return a - b

    def multiply(self, a: int, b: int) -> int:
        """Returns the product of two integers."""
        self._validate_input(a, b)
        return a * b

    def divide(self, a: int, b: int) -> float:
        """
        Returns the quotient of two integers.
        Raises ValueError if trying to divide by zero.
        """
        self._validate_input(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b