from pythonproblems.functions.utils import Input


def character_ascii_value() -> None:
    """
    This program gets the ASCII value from a character.
    Author: Gustavo Assi Alencar.
    Date:   13/11/2025.
    """

    # Step 1: Get from user the character.
    character = Input.get_character("Type a character: ")

    # Step 2: Return the ASCII value.
    ascii_value = ord(character)

    # Step 3: Display result.
    print(f'>>> ASCII value for "{character}": {ascii_value}')


def main() -> None:
    character_ascii_value()


if __name__ == "__main__":
    main()
