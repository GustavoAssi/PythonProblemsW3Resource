from utils import Input


def number_input_validator() -> None:
    """
    This program inputs a number and generates an error message if it is not a number.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: Get a number (as a string):
    number = Input.get_string("Type a number: ", stripped=True)

    # Step 2: Check if is a number.
    number_count = 0
    all_characters_passed = True
    for character in number:
        if not (character.isnumeric() or character in ".,"):
            print("Is not a number!")
            all_characters_passed = False
            break
        elif character.isnumeric():
            number_count += 1

    if number_count > 1 and all_characters_passed:
        print("Is a number")


def main() -> None:
    number_input_validator()


if __name__ == "__main__":
    main()
