# Author: William Richmond
# Date: 2024-11-02
# Class: CYBR-260-45
# Assignment: Summing Numbers Unit Tests
# Description: Unit tests for SummingManager functions in Summing_numbers.

import unittest
from summing_manager import SummingManager

class TestSummingManager(unittest.TestCase):
    """Unit tests for SummingManager class methods."""

    def setUp(self):
        """Set up a SummingManager instance for testing."""
        self.manager = SummingManager()

    def test_calculate_sum(self):
        """Test sum calculation."""
        self.assertEqual(self.manager.calculate_sum(5, 10, 2), 17)

    def test_calculate_multiplication(self):
        """Test multiplication calculation."""
        self.assertEqual(self.manager.calculate_multiplication(5, 10, 2), 100)

    def test_calculate_division_multiplication(self):
        """Test division-multiplication calculation with non-zero divisor."""
        self.assertEqual(self.manager.calculate_division_multiplication(10, 5, 2), 4)

    def test_division_by_zero(self):
        """Test division-multiplication with zero divisor, expecting 'undefined'."""
        self.assertEqual(self.manager.calculate_division_multiplication(10, 0, 2), "undefined (cannot divide by zero)")

if __name__ == "__main__":
    unittest.main()
