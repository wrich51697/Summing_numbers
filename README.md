# Summing_numbers

Summing_numbers is a Python program that takes a user’s name and three numbers, performing calculations (sum, multiplication, and a division-multiplication operation). It allows the user to repeat calculations without re-entering their name.

## Features

- Prompts for user input of three numbers.
- Performs sum, multiplication, and custom division-multiplication calculations.
- Provides error handling for invalid input.
- Allows repeated calculations without re-entering the user’s name.

## Project Structure

- **summing_manager.py**: Contains `SummingManager` class with calculation and input retrieval methods.
- **main.py**: Runs the main application loop, calling `SummingManager`.
- **demo.py**: Demonstrates functionality with pre-set inputs.
- **test_summing_manager.py**: Unit tests for `SummingManager`.
- **requirements.txt**: Lists dependencies.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Summing_numbers.git
    cd Summing_numbers
    ```

2. Install required packages (if any are added):

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the main program:

```bash
python main.py
```

# Demo

Run the demo to see Summing_numbers in action with simulated inputs:

```bash
python demo.py
```
# Testing

Run the unit tests to verify that each function in `SummingManager` works correctly:

```bash
python -m unittest test_summing_manager.py
```