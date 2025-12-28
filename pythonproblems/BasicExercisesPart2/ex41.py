from pythonproblems.functions.utils import Input


def is_overflow(value: float) -> bool:
    """
    This function checks if a value is a overflow or not.
    :param value: the value to check if is overflow.
    :return: True or False.
    """
    return value >= 10 ** 80


def sum_with_overflow_check() -> None:
    """
    This program computes and print the sum of two given integers.
    In the event that the given integers or the sum exceed 80 digits, print "overflow".
    Author: Gustavo Assi Alencar.
    Date:   25/12/2025.
    """

    # Step 1: Get x and y.
    x = Input.get_float_number("Type value of x (float number): ")
    y = Input.get_float_number("Type value of y (float number): ")

    # Step 2: Check if x + y is a overflow case.
    case = "overflow" if is_overflow(x + y) else "not overflow"
    print(f"{x} + {y} = {x + y} ({case})")


def main() -> None:
    sum_with_overflow_check()


if __name__ == "__main__":
    main()
