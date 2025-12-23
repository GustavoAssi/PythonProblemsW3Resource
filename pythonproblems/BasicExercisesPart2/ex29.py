from math import sqrt
from pythonproblems.functions.utils import Input


def find_gcd(x, y) -> int:
    """
    Finds the G.C.D (Greatest Common Divisor) from two numbers.
    :param x: 1º number.
    :param y: 2º number.
    return: G.C.D value.
    """
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


def common_divisors_finder() -> None:
    """
    This program finds common divisors between two numbers in a given pair.
    Author: Gustavo Assi Alencar.
    Date:   08/12/2025.
    """

    # Step 1: Get the numbers from user.
    x = Input.get_integer_number("Value of x (positive integer): ", must_be_positive=True)
    y = Input.get_integer_number("Value of y (positive integer): ", must_be_positive=True)

    # Step 2: Evaluate the common divisors.
    if x >= y:
        x, y = y, x
    gcd = find_gcd(x, y)
    
    # Step 3: Find the divisors from G.C.D to find the common divisors from x and y.
    common_divisors = []
    for factor in range(1, gcd + 1):
        if gcd % factor == 0:
            common_divisors.append(factor)

    print(f">>> Common divisors: {common_divisors}")


def main() -> None:
    common_divisors_finder()


if __name__ == "__main__":
    main()
