from utils import Input


def is_numeric_string(string: str) -> bool:
    """
    Function to check if a string is numeric or not.
    :param string: string to check if is numeric or not.
    :return: True or False.
    """
    string_parts = string.split(".")
    string_parts = string.split(",") if len(string_parts) == 1 else string_parts
    for part in string_parts:
        if not part.isnumeric():
            return False
    return True


def check_if_a_string_is_numeric() -> None:
    """
    This program checks if whether a string is numeric.
    Author: Gustavo Assi Alencar.
    Date:   13/11/2025.
    """

    # Step 1: Get a string from user.
    string = Input.get_string("Type a string: ", stripped=True)

    # Step 2: Check if string is numeric.
    if is_numeric_string(string):
        print(f"User typed a numeric string.")
    else:
        print(f"User typed a non numeric string.")


def main() -> None:
    check_if_a_string_is_numeric()


if __name__ == "__main__":
    main()
