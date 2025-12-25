from pythonproblems.functions.utils import Input


def get_number_of_carries(x: int, y: int) -> int:
    """
    Returns the number of carries of digits during computation of x + y.
    Where x and y are positive integers.
    :param x: 1º positive integer.
    :param y: 2º positive integer.
    :return: number of carry operations.
    """

    counter = 0

    # Step 1: If x and y are equal to zero, then there is no carry operations.
    if x == 0 and y == 0:
        return 0
    
    # Step 2: Let the current digit be evaluated
    digit = 0
    for _ in range(10):
        digit = x % 10 + y % 10 + digit
        if digit > 9:
            digit = 1
        else:
            digit = 0
        counter += digit
        x //= 10
        y //= 10

    return counter


def carry_operations_count() -> None:
    """
    This program counts the number of carry operations for each addition problem.
    Author: Gustavo Assi Alencar.
    Date:   23/12/2025.
    """

    # Step 1: Get two integer x and y.
    x = Input.get_integer_number("Value of x (positive value): ", must_be_positive=True)
    y = Input.get_integer_number("Value of y (positive value): ", must_be_positive=True)

    # Step 2: Count carry operations when compute x + y.
    number_of_carries = get_number_of_carries(x, y)
    print(f">>> Number of carries: {number_of_carries}")
 

def main() -> None:
    carry_operations_count()


if __name__ == "__main__":
    main()
