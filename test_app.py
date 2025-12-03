# test_app.py

import unittest
from app import Calculator

class TestCalculator(unittest.TestCase):
    """Test suite for the Calculator class in app.py."""

    # Setup Method (executed before EVERY test method)
    def setUp(self):
        """Initialize the Calculator object before each test."""
        self.calc = Calculator()
        # print("\nSetting up a new Calculator object...") # Commented out for cleaner output

    # --- POSITIVE TEST CASES ---

    def test_add_positive_numbers(self):
        """Test adding two positive integers."""
        self.assertEqual(self.calc.add(10, 5), 15, "Should be 15")

    def test_add_negative_and_positive(self):
        """Test adding a negative and a positive number."""
        self.assertEqual(self.calc.add(-10, 5), -5, "Should be -5")

    # --- NEGATIVE TEST CASES / EXCEPTION HANDLING ---

    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises a specific ValueError."""
        # Check that the specific exception is raised
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)

        # Verify the exception message
        self.assertTrue('Cannot divide by zero' in str(context.exception))

    def test_power_with_non_numeric_input_raises_error(self):
        """Test that non-numeric inputs for power raise a TypeError."""
        with self.assertRaises(TypeError) as context:
            self.calc.power(2, "x")
        
        self.assertTrue('must be numbers' in str(context.exception))

    # Teardown Method (executed after EVERY test method)
    def tearDown(self):
        """Cleanup after each test."""
        del self.calc
        # print("Tearing down Calculator object...") # Commented out for cleaner output

# This allows the tests to be run directly from the command line
if __name__ == '__main__':
    unittest.main()