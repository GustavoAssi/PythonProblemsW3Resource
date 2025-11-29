from pythonproblems.functions.utils import Input


def binary_with_leading_zeroes() -> None:
    """
    This program converts an integer to binary that keeps leading zeros.
    Author: Gustavo Assi Alencar.
    Date:   24/11/2025.
    """

    # Step 1: Get an integer from user.
    integer = Input.get_integer_number("Type an integer number: ")

    # Step 2: Format this number in binary with leading zeros.
    print(format(integer, "08b"))


def main():
    binary_with_leading_zeroes()


if __name__ == "__main__":
    main()
