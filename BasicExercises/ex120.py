from utils import Input


def string_formatter_with_length_limit() -> None:
    """
    This program formats a specified string and limit the length of a string.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: Get a string from user.
    string = Input.get_string("Type a string: ", stripped=True)
    number_format = Input.get_integer_number("Type a number to format: ", must_be_positive=True)

    # Step 2: Display string with specified format.
    print("")
    print(f">>> Original string: {string}")
    print(f">>> First {number_format} of the string: {string[:number_format + 1]}")


def main() -> None:
    string_formatter_with_length_limit()


if __name__ == "__main__":
    main()
