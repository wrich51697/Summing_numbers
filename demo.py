# Author: William Richmond
# Date: 2024-11-02
# Class: CYBR-260-45
# Assignment: Summing Numbers Demo
# Description: Demonstrates the functionality of Summing_numbers.

from summing_manager import SummingManager

def run_demo():
    """Runs a demonstration of the SummingManager functionality with preset inputs."""

    manager = SummingManager()
    name = "Demo User"
    print(f"Results for {name}:")

    # Sample numbers
    num1, num2, num3 = 5, 10, 2

    print(f"Sum: {manager.calculate_sum(num1, num2, num3)}")
    print(f"Multiplication: {manager.calculate_multiplication(num1, num2, num3)}")
    print(f"Division-Multiplication: {manager.calculate_division_multiplication(num1, num2, num3)}")

if __name__ == "__main__":
    run_demo()
