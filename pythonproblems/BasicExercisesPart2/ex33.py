from pythonproblems.functions.utils import Input


def sum_digit_count() -> None:
    """
    This program computes the digit number of the sum of two given integers.
    Author: Gustavo Assi Alencar.
    Date:   23/12/2025.
    """

    # Step 1: Get the numbers x and y.
    x = Input.get_integer_number("Type the value of x (integer value): ")
    y = Input.get_integer_number("Type the value of y (integer value): ")
    
    # Step 2: Sum the digits of x + y.
    s = str(x + y).replace('-', '')
    count_of_digits = len(s)
    print(f">>> {x} + {y} = {x + y}")
    print(f">>> count of digits of the sum: {count_of_digits}")


def main() -> None:
    sum_digit_count()


if __name__ == "__main__":
    main()
