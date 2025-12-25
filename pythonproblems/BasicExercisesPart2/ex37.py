import itertools
from pythonproblems.functions.utils import Input


def sum_combinations_counter() -> None:
    """
    This program reads an integer n and finds the number of combinations of 
    a,b,c and d (0 = a,b,c,d = 9) where (a + b + c + d) will be equal to n.
    Author: Gustavo Assi Alencar.
    Date:   23/12/2025.
    """

    # Step 1: Get a number n.
    n = Input.get_integer_number("Type a value of n (1 <= n <= 50): ", must_be_positive=True)

    # Step 2: Generate and count combinations.
    count = 0
    for (i, j, k, l) in itertools.product(range(10), range(10), range(10), range(10)):
        if i + j + k + l == n:
            print(f"{i} + {j} + {k} + {l} = {i + j + k + l}")
            count += 1

    print(f"\n>>> Total combinations: {count}")


def main() -> None:
    sum_combinations_counter()


if __name__ == "__main__":
    main()
