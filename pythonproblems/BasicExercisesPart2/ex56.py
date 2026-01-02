import re
from pythonproblems.functions.utils import Input


def sum_of_numbers_in_text() -> None:
    """
    This program computes the sum all numerical values (positive integers) embedded in a sentence.
    Author: Gustavo Assi Alencar.
    Date:   28/12/2025.
    """

    # Step 1: Get a sentence.
    sentence = Input.get_string("Type a sentence: ")

    # Step 2: Sum all numeric values.
    sum_of_numeric_values = sum(map(int, re.findall(r'[0-9]+', sentence)))
    print(f">>> The sum of all numeric values are: {sum_of_numeric_values}")


def main() -> None:
    sum_of_numbers_in_text()


if __name__ == "__main__":
    main()
