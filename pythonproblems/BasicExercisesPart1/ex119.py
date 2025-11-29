from pythonproblems.functions.utils import Input


def round_float_to_decimals() -> None:
    """
    This program rounds a floating-point number to a specified number of decimal places.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: Get a float number and a number of decimal places from user.
    number = Input.get_float_number("Type a float number: ")
    decimal_places = Input.get_integer_number("Type a number of decimal places: ", must_be_positive=True)

    # Step 2: Round the number and display the result.
    print(f">>> {round(number, decimal_places)}")


def main() -> None:
    round_float_to_decimals()


if __name__ == "__main__":
    main()
