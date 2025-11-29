from pathlib import Path


def word_frequency_counter() -> None:
    """
    This program prints long text, converts it to a list, and
    prints all the words and the frequency of each word.
    Author: Gustavo Assi Alencar.
    Date:   26/11/2025.
    """

    # Step 1: Get the text from somewhere.
    text_file = Path(__file__).parent / "ex6_text.txt"

    # Step 2: Convert this text into a string.
    with open(text_file, 'r') as file:
        full_text = file.read()

    # Step 3: With the text as a string, split the words.
    words = [
        word.replace(',', '').replace('.', '').replace('\"', "")
        for word in full_text.split()
    ]

    # Step 4: In the splited string, count each word.
    # (Use a dictionary or use the collections module can help)
    word_conter = {}
    for word in words:
        if word not in word_conter:
            word_conter[word] = 0
        word_conter[word] += 1

    # Step 5: Display the results.
    for word, frequency in word_conter.items():
        print(f">>> word: {word} -> {frequency} times.")


def main() -> None:
    word_frequency_counter()


if __name__ == "__main__":
    main()
