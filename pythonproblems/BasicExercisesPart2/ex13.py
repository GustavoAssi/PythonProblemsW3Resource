from pythonproblems.functions.utils import Input


def get_two_digit_number() -> str:
    """
    Function two return two digits number in string format.
    """
    while True:
        number = Input.get_string("Type a two digit number: ", stripped=True)
        number_size = len(number)
        if number_size != 2:
            print(f"Number must be two digits!")
        elif '0' in number:
            print(f"Number should not have zero!")
        else:
            return number


def two_digit_letter_combos() -> None:
    """
    This program gets all possible two-digit letter
    combinations from a 1-9 digit string.
    Author: Gustavo Assi Alencar.
    Date:   29/11/2025.
    """

    # Step 1: Set a map of digits.
    letters = {
        "1": "abc", "2": "def", "3": "ghi",
        "4": "jkl", "5": "mno", "6": "pqrs",
        "7": "tuv", "8": "wxy", "9": "z"
    }

    # Step 2: Get a two digit value.
    number = get_two_digit_number()

    # Step 3: Display the combinations.
    letters_1 = letters[number[0]]
    letters_2 = letters[number[1]]
    combinations = []
    for first_letter in letters_1:
        for second_letter in letters_2:
            combinations.append(f"{first_letter}{second_letter}")

    print(f">>> {combinations}")


def main() -> None:
    two_digit_letter_combos()


if __name__ == "__main__":
    main()
