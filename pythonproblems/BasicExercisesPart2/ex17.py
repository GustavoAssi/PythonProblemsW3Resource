from pythonproblems.functions.utils import Input


def is_strobogrammatic(n: int) -> bool:
    """
    Returns True if the number is strobogrammatic, False otherwise.
    :param n: the integer number to check if is strobogrammatic or not.
    """
    number = f'{n}'
    strobogrammatic_map = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
    encoded_number = ""
    for digit in number:
        try:
            encoded_number += strobogrammatic_map[digit]
        except KeyError:
            return False

    return encoded_number[::-1] == number


def strobogrammatic_numbers() -> None:
    """
    This program gets all strobogrammatic numbers that are of length n.
    A strobogrammatic number is a number whose numeral is rotationally
    symmetric, so that it appears the same when rotated 180 degrees.
    In other words, the numeral looks the same right-side up and
    upside down (e.g., 69, 96, 1001).
    Author: Gustavo Assi Alencar.
    Date:   29/11/2025.
    """

    # Step 1: Get the number of digits.
    number_of_digits = Input.get_integer_number("Type the number of digits: ", must_be_positive=True)

    # Step 2: Get all strobogrammatic numbers with the number of digits passed by user.
    strobogrammatics = []
    for n in range(10**(number_of_digits - 1), 10**number_of_digits):
        if is_strobogrammatic(n):
            strobogrammatics.append(n)

    # Step 3: Display the results:
    print(f">>> {strobogrammatics}")


def main() -> None:
    strobogrammatic_numbers()


if __name__ == "__main__":
    main()
