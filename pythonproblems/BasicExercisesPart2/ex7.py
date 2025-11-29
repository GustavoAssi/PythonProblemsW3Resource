from pathlib import Path


def character_frequency_in_file() -> None:
    """
    This program count the number of each character in a text file.
    Author: Gustavo Assi Alencar.
    Date:   26/11/2025.
    """

    # Step 1: Get the text file from somewhere.
    text_file = Path(__file__).parent / "ex7_text.txt"

    # Step 2: Count the number of characters from text file.
    with open(text_file, "r") as file:
        text = file.read().upper()

    # Step 3: Count all characters.
    characters = {}
    for character in text:
        if character not in characters:
            characters[character] = 0
        characters[character] += 1

    # Step 4: Display results.
    for character, frequency in characters.items():
        print(f">>> character {character} -> {frequency} times")


def main() -> None:
    character_frequency_in_file()


if __name__ == "__main__":
    main()
