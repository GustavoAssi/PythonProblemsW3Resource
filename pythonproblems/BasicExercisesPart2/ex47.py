from pathlib import Path


def word_frequency_and_length() -> None:
    """
    This program reads text (only alphabetical characters and spaces) and prints two words.
    The first word is the one that appears most often in the text. 
    The second one is the word with the most letters.
    Author: Gustavo Assi Alencar.
    Date:   25/12/2025.
    """

    # Step 1: Read the ex47.txt file.
    file_path = Path(__file__).parent / "ex47.txt"
    with open(file_path, "r") as file:
        text = file.read()

    # Step 2: Get words frequency
    words = text.replace("\n", " ").replace(".", " ").replace(",", " ").split(" ")
    words_frequency = {}
    for word in words:
        if word == "":
            continue
        if word not in words_frequency:
            words_frequency[word] = 1
        else:
            words_frequency[word] += 1

    # Step 3: Get the one that appears most.
    most_repeated_word = max(words_frequency.items(), key=lambda word: word[1])

    # Step 4: Get the words with more letters.
    longest_word = max(words_frequency.items(), key=lambda word: len(word[0]))
    
    # Step 5: Display results.
    for word, frequency in words_frequency.items():
        print(f"--> {word}: {frequency} times")

    print(f">>> The most repeated word: {most_repeated_word[0]} ({most_repeated_word[1]} times)")
    print(f">>> The longest word: {longest_word[0]} ({longest_word[1]} times)")


def main() -> None:
    word_frequency_and_length()


if __name__ == "__main__":
    main()
