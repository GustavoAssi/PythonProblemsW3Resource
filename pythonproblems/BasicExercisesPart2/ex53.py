from pythonproblems.functions.utils import Input
from pythonproblems.BasicExercisesPart2.ex52 import term_is_prime


def is_even_number(number: int) -> bool:
    """
    Checks if a number is even or not.
    :param number: an integer number that can be even or not.
    :return: True if number is even, False otherwise.
    """

    return number % 2 == 0


def get_even_number() -> int:
    """
    Returns an even number from terminal input.
    :return: an even number.
    """

    while True:
        n = Input.get_integer_number("Type an even number: ", must_be_positive=True)
        if is_even_number(n):
            return n
        else:
            print(f"{n} is not an even number! Try again...")


def primes(start=2, stop=None):
    """
    Prime numbers generator.
    """

    n = start
    while stop is None or n < stop:
        if term_is_prime(n):
            yield n
        n += 1


def goldbach_partition_counter() -> None:
    """
    This program accepts an even number (>=4, Goldbach number) from the user and 
    creates combinations which express the given number as a sum of two prime numbers. 
    Author: Gustavo Assi Alencar.
    Date:   28/12/2025.
    """

    # Step 1: Get a even number.
    n = get_even_number()

    # Step 2: Check Goldbach conjecture.
    combinations = []
    for i in primes(stop=n):
        for j in primes(start=i + 1, stop=n):
            if i + j == n:
                combination = f"{i} + {j} = {n}"
                print(f">>> {combination}")
                if combination not in combinations:
                    combinations.append(combination)

    print(f">>> Total combinations: {len(combinations)}")

def main() -> None:
    goldbach_partition_counter()


if __name__ == "__main__":
    main()
