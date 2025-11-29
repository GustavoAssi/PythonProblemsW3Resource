from pythonproblems.functions.utils import Input


def lower_case_letters_checker() -> None:
    """
    This program checks whether lowercase letters exist in a string.
    Author: Gustavo Assi Alencar.
    Date:   20/11/2025.
    """

    # Step 1: Get a string from user.
    string = Input.get_string("Type any string: ", stripped=True)

    # Step 2: Check if any character is lowercase.
    lowercase_chars = []
    for character in string:
        if character.islower():
            lowercase_chars.append(character)

    if len(lowercase_chars) > 0:
        print(f">>> String has a few lowercase characters: {lowercase_chars}")
    else:
        print(">>> String hasn't any lowercase characters.")

def main():
    lower_case_letters_checker()


if __name__ == "__main__":
    main()
