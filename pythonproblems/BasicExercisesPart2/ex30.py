from pythonproblems.functions.utils import Input


def reverse_number(number: int) -> int:
    """
    Returns a integer with digits in reverse order.
    :param number: the number to reverse digits.
    :return: The integer with reversed digits.
    """
    number_str = str(number)
    return int(number_str[::-1])


def is_palindrome_number(number: int) -> bool:
    """
    Checks if a number is a palindrome.
    :param number: the number to check is a palindrome or not.
    :return: True or False.
    """
    number_str = str(number)
    return number_str == number_str[::-1]


def palindrome_sum_iteration() -> None:
    """
    This program reverses the digits of a given number and add them to the original.
    Repeat this procedure if the sum is not a palindrome.
    Author: Gustavo Assi Alencar.
    Date:   08/12/2025.
    """

    # Step 1: Get the number from user.
    number = Input.get_integer_number("Type an positive integer number: ", must_be_positive=True)
    reversed_number = reverse_number(number)
    result = number + reversed_number

    # Step 2: Start the process to reverse digits and sum until sum is not a palindrome.
    while not is_palindrome_number(result):
        print(f">>> {result}")
        reversed_number = reverse_number(result)
        result += reversed_number

    # Step 3: Display final result.
    print(f">>> final result: {result}")


def main() -> None:
    palindrome_sum_iteration()


if __name__ == "__main__":
    main()
