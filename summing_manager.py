# Author: William, Richmond
# Date: 2024-11-02
# Class: CYBR-260-45
# Assignment: Modularized Summing Numbers Program
# Description: This module contains the SummingManager class for retrieving inputs and performing calculations.

import logging

# Set up logging
logging.basicConfig(filename='summing_manager.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class SummingManager:
    """Handles operations related to user input and number calculations."""

    @staticmethod
    def get_user_name():
        """Request and return the user's name."""
        return input("Please enter your name: ")

    @staticmethod
    def get_numbers():
        """Request three numbers from the user and return them as floats with error handling."""
        while True:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                num3 = float(input("Enter the third number: "))
                return num1, num2, num3
            except ValueError as e:
                logging.error(f"Invalid input: {e}")
                print("Invalid input! Please enter numeric values.")

    @staticmethod
    def calculate_sum(num1, num2, num3):
        """Calculate and return the sum of three numbers."""
        return num1 + num2 + num3

    @staticmethod
    def calculate_multiplication(num1, num2, num3):
        """Calculate and return the product of three numbers."""
        return num1 * num2 * num3

    @staticmethod
    def calculate_division_multiplication(num1, num2, num3):
        """Divide the first number by the second, then multiply by the third. Return result or error message."""
        if num2 != 0:
            return (num1 / num2) * num3
        else:
            return "undefined (cannot divide by zero)"

