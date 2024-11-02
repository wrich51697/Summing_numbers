# Author: William Richmond
# Date: 2024-11-02
# Class: CYBR-260-45
# Assignment: Summing Numbers Application
# Description: Main application to manage user interactions and calculations in Summing_numbers.

from summing_manager import SummingManager

class SummingApp:
    """Main application to handle user interactions and manage repeated calculations."""

    def __init__(self):
        """Initialize SummingManager and get the user's name."""
        self.manager = SummingManager()
        self.name = self.manager.get_user_name()

    def print_results(self, sum_result, multiply_result, division_multiplication_result):
        """Prints results for calculations."""
        print(f"\nResults for {self.name}:")
        print(f"Sum of the numbers: {sum_result}")
        print(f"Multiplication of the numbers: {multiply_result}")
        print(f"Division of the first by the second, multiplied by the third: {division_multiplication_result}")

    @staticmethod
    def get_menu_choice():
        """Prompt the user for a menu choice and validate the input."""
        while True:
            try:
                choice = int(input("\nWould you like to perform another calculation? (1 = Yes, 2 = No): "))
                if choice in (1, 2):
                    return choice
                else:
                    print("Invalid choice! Please select either 1 or 2.")
            except ValueError:
                print("Invalid input! Please enter a number (1 or 2).")

    def run(self):
        """Run the main loop to perform calculations until the user chooses to exit."""
        while True:
            num1, num2, num3 = self.manager.get_numbers()

            # Perform calculations
            sum_result = self.manager.calculate_sum(num1, num2, num3)
            multiply_result = self.manager.calculate_multiplication(num1, num2, num3)
            division_multiplication_result = self.manager.calculate_division_multiplication(num1, num2, num3)

            # Display the results
            self.print_results(sum_result, multiply_result, division_multiplication_result)

            # Ask the user if they want to continue
            choice = self.get_menu_choice()
            if choice == 2:
                print("Thank you for using the program. Goodbye!")
                break

if __name__ == "__main__":
    app = SummingApp()
    app.run()
