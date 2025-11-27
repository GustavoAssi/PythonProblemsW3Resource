from utils import Input


def decimal_to_hexadecimal() -> None:
    """
    This program converts decimal to hexadecimal.
    Author: Gustavo Assi Alencar.
    Date:   24/11/2025.
    """

    # Step 1: Get an integer number from the user.
    integer = Input.get_integer_number("Type an integer number: ")

    # Step 2: Display the result of number in hexadecimal system.
    print(f">>> Same number in hexadecimal system: {hex(integer)}")


def main():
    decimal_to_hexadecimal()


if __name__ == "__main__":
    main()
