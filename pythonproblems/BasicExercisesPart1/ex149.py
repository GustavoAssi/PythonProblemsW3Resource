from pythonproblems.functions.utils import Input


def cube_sum_of_smaller_integers() -> None:
    """
    This program takes a positive integer and returns the sum of
    the cube of all positive integers smaller than the specified number.
    Author: Gustavo Assi Alencar.
    Date:   25/11/2025.
    """

    # Step 1: Get an integer.
    n = Input.get_integer_number("Type an integer number greater then 2: ", must_be_positive=True)

    # Step 2: Calculate the sum of cubes less than the integer from Step 1.
    if n > 2:
        s = ((n - 1) * n / 2) ** 2
        print(f">>> 1³ + ... + {n - 1}³ = {int(s)}")
    else:
        print(f">>> Enter a value greater then 2, please.")


def main():
    cube_sum_of_smaller_integers()


if __name__ == "__main__":
    main()
