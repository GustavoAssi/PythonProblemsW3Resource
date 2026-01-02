from pythonproblems.functions.utils import Input


def get_eight_digits_number() -> str:
    """
    Get from termnal an eight digits number.
    :return: the eight digits number in string format.
    """
    while True:
        number = Input.get_string("Input a 8 digit number: ", stripped=True)
        if len(number) == 8 and number.isnumeric():
            return number
        elif not number.isnumeric():
            print("Invalid input: input is not an integer number.")
        elif len(number) != 8:
            print("Invalid input: number must have 8 digits.")


def largest_smallest_integer_difference() -> None:
    """
    This program determines the difference between the largest and 
    smallest integers created by 8 numbers from 0 to 9.
    The number that can be rearranged shall start with 0 as in 00135668.
    Author: Gustavo Assi Alencar.
    Date:   28/12/2025.
    """

    # Step 1: Get an 8 digit integer number.
    number = get_eight_digits_number()

    # Step 2: Get the smallest and the largest number formed by this digits.
    smallest = int("".join(sorted(list(number))))
    largest = int("".join(sorted(list(number), reverse=True)))

    # Step 3: Display the difference between the largest and the smallest.
    print(f">>> Smallest: {smallest}")
    print(f">>> Largest: {largest}")
    print(f">>> Difference: {largest - smallest}")



def main() -> None:
    largest_smallest_integer_difference()


if __name__ == "__main__":
    main()
