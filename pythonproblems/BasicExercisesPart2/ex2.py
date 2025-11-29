from itertools import permutations


def all_unique_strings() -> None:
    """
    This program creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'u'.
    Ensure that each character is used only once.
    Author: Gustavo Assi Alencar.
    Date:   26/11/2025.
    """

    # Step 1: Display all possible strings using letters 'a', 'e', 'i', 'o' and 'u'.
    words = []
    for word in permutations(['a', 'e', 'i', 'o', 'u']):
        string = "".join(word)
        words.append(string)
        print(string)

    # Step 2: Amount of possible strings.
    print(f">>> Total of possible strings: {len(words)}")
    assert len(words) == 120, "In this case, we should got 120 words"


def main() -> None:
    all_unique_strings()


if __name__ == "__main__":
    main()
