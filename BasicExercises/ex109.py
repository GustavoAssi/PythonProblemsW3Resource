from utils import Input


def number_analyser() -> None:
    """
    This program checks if a number is positive, negative or zero.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: Get the number from user.
    number = Input.get_float_number("Enter a number: ")

    # Step 2: Analyse the number.
    if number > 0:
        print("Number is positive")
    elif number == 0:
        print("Number is equal to zero")
    else:
        print("Number is negative")


def main() -> None:
    number_analyser()


if __name__ == "__main__":
    main()
