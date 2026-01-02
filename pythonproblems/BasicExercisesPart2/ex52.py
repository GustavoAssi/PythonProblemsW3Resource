from pythonproblems.functions.utils import Input


def term_is_prime(term: int) -> bool:
    """
    Returns True if a term is a prime number.
    :param term: a natural number.
    :return: if the term is prime or not.
    """
    if term in [2, 3, 5, 7]:
        return True
    elif any([term % factor == 0 for factor in [2, 3, 5, 7]]):
        return False
    else:
        for factor in range(11, int(term**0.5) + 1):
            if term % factor == 0 and term != factor:
                return False
        return True 
    

def sum_of_first_primes() -> None:
    """
    This program computes the sum of the first n prime numbers.
    Author: Gustavo Assi Alencar.
    Date:   28/12/2025.
    """

    # Step 1: Get an integer number.
    n = Input.get_integer_number("Value of n: ", must_be_positive=True)

    # Step 2: Compute the sum of the first n prime numbers.
    sum_of_primes = 0
    counter = 0
    term = 1
    while counter < n:
        if term_is_prime(term):
            print(f">>> {term} is prime number!")
            sum_of_primes += term
            counter += 1
        term += 1

    # Step 3: Display the sum of primes.
    print(f">>> Sum of first {n} primes: {sum_of_primes}")


def main() -> None:
    sum_of_first_primes()


if __name__ == "__main__":
    main()
