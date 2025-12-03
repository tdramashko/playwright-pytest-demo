# app.py

class Calculator:
    """A simple calculator class for testing."""

    def add(self, a, b):
        """Returns the sum of two numbers."""
        return a + b

    def divide(self, a, b):
        """Returns the quotient of two numbers. Handles division by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def power(self, base, exponent):
        """Calculates base raised to the power of exponent."""
        if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
             raise TypeError("Base and exponent must be numbers.")
        return base ** exponent