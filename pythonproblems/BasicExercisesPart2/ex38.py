from pythonproblems.functions.utils import Input


def get_all_primes(n: int) -> list:
    """
    Returns all prime numbers until a number n.
    :param n: a positive integer.
    :return: all prime numbers until n.
    """

    # Apply the Sieve of Erasthostenes algorithm.
    prime_numbers = []
    for number in range(2, n + 1):
        case_1 = number == 2 or number == 3 or number == 5 or number == 7
        case_2 = not (number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0)
        if case_1 or case_2:
            prime_numbers.append(number)

    return prime_numbers


def count_prime_numbers() -> None:
    """
    This program prints the number of prime numbers that 
    are less than or equal to a given number.
    Author: Gustavo Assi Alencar.
    Date:   23/12/2025.
    """

    # Step 1: Get a positive integer n.
    n = Input.get_integer_number("Type a positive integer: ", must_be_positive=True)

    # Step 2: Count the number of prime numbers until n.
    primes = get_all_primes(n)
    print(f">>> Prime numbers: {primes}")
    print(f">>> Number of primes: {len(primes)}")


def main() -> None:
    count_prime_numbers()


if __name__ == "__main__":
    main()
