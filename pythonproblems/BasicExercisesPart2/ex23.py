from pythonproblems.functions.utils import Input


def subtract_sum_of_digits() -> None:
    """
    This program accepts a positive number and subtracts from it the sum of its digits, and so on.
    Continue this operation until the number is positive.
    Author: Gustavo Assi Alencar.
    Date:   08/12/2025.
    """

    # Step 1: Get a number from user.
    number = Input.get_integer_number("Type an positive integer number: ", must_be_positive=True)

    # Step 2: Start the subtraction process.
    while number > 0:
        sum_of_digits = sum([int(value) for value in f"{number}"])
        print(f">>> {number} - {sum_of_digits} = {number - sum_of_digits}")
        number -= sum_of_digits


def main() -> None:
    subtract_sum_of_digits()


if __name__ == "__main__":
    main()
