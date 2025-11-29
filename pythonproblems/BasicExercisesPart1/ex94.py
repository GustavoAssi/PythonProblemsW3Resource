from pythonproblems.functions.utils import Input


def string_bytes_to_integers() -> None:
    """
    This program converts the bytes in a given string to a list of integers.
    Author: Gustavo Assi Alencar.
    Date:   13/11/2025.
    """

    # Step 1: Get a string from user.
    string = Input.get_string("Type a string: ", stripped=True)

    # Step 2: Get the byte object from string.
    byte_list = [ord(character) for character in string]

    # Step 3: Display the results.
    print(f">>> String in bytes list format: {byte_list}")


def main() -> None:
    string_bytes_to_integers()


if __name__ == "__main__":
    main()
