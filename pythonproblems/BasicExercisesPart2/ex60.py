from pythonproblems.functions.utils import Input


def treat_word(word: str) -> str:
    word = word.strip()
    for character in word:
        if not character.isalpha():
            word = word.replace(character, '')
    return word


def cut_words_by_length() -> None:
    """
    This program cuts out words of 3 to 6 characters length from a given sentence not more than 1024 characters.
    Author: Gustavo Assi Alencar.
    Date:   28/12/2025.
    """

    # Step 1: Get the sentence.
    sentence = Input.get_string("Input a sentence: ", stripped=True)

    # Step 2: If sentence is not more than 1024 characters, get the words from sentence.
    if len(sentence) <= 1024:
        words = [treat_word(word) for word in sentence.split()]

        # Step 3: Filter the words with length between 3 and 6 characters.
        filtered_words = [word for word in words if 3 <= len(word) <= 6]
        print(f">>> Words with length between 3 and 6 characters: {filtered_words}")
    else:
        print(">> Sentence has more than 1024 characters.")
    

def main() -> None:
    cut_words_by_length()


if __name__ == "__main__":
    main()
