from pythonproblems.functions.utils import Input


def factorial_trainling_zeros() -> None:
    """
    This program finds the number of zeros at the end of a factorial of
    a given positive number. Range of the number(n): (1 <= n <= 2*109).
    Author: Gustavo Assi Alencar.
    Date:   29/11/2025.
    """

    # Step 1: Get the value of n.
    n = Input.get_integer_number("Type the value of n: ", must_be_positive=True)
    original_n = n

    # Step 2: Start the count of zeros from n!.
    count = 0
    while n > 0:
        n //= 5
        count += n
    print(f"Numbers of zeros from {original_n}! -> {count} zeros.")


def main() -> None:
    factorial_trainling_zeros()


if __name__ == "__main__":
    main()
