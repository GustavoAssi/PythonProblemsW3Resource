from pythonproblems.functions.utils import Input


def even_or_odd_divisors() -> None:
    """
    This program finds the total number of even or odd divisors of a given integer.
    Author: Gustavo Assi Alencar.
    Date:   08/12/2025.
    """

    # Step 1: Get a number from user.
    n = Input.get_integer_number("Type a positive integer number: ", must_be_positive=True)

    # Step 2: Get the total number of divisors of the number.
    total_number_of_divisors = len([factor for factor in range(1, n + 1) if n % factor == 0])
    print(f">>> Total number of divisors: {total_number_of_divisors} divisors")


def main() -> None:
    even_or_odd_divisors()


if __name__ == "__main__":
    main()
