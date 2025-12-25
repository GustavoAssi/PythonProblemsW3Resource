from pythonproblems.functions.utils import Input


def can_form_a_triangle(side_1: int, side_2: int, side_3: int) -> bool:
    """
    Returns True if it's possible to form a triangle given the sides.
    :param side_1: 1º side of triangle.
    :param side_2: 2º side of triangle.
    :param side_3: 3º side of triangle.
    :return: True or False.
    """

    return side_1 <= side_2 + side_3 and side_2 <= side_1 + side_3 and side_3 <= side_1 + side_2


def classify_triangle(side_1: int, side_2: int, side_3: int) -> None:
    """
    Classifies a triangle given the sides: Isosceles, Equilateral, Scalene or Right triangle.
    :param side_1: 1º side of triangle.
    :param side_2: 2º side of triangle.
    :param side_3: 3º side of triangle.
    """

    if side_1 == side_2 and side_2 == side_3:
        print(f">>> Equilateral Triangle")
    elif side_1 != side_2 and side_2 != side_3 and side_1 != side_3:
        print(f">>> Scalene Triangle")
    else:
        print(f">>> Isosceles Triangle")

    if side_1**2 == side_2**2 + side_3**2 or side_2**2 == side_1**2 + side_3**2 or side_3**2 == side_1**2 + side_2**2:
        print(f">>> Right Triangle")


def right_triangle_validator() -> None:
    """
    This program checks whether three given lengths (integers) of three sides form a right triangle.
    Author: Gustavo Assi Alencar.
    Date:   23/12/2025.
    """

    # Step 1: Get the sides from the triangle.
    side_1 = Input.get_integer_number("Type the 1º side of the triangle: ", must_be_positive=True)
    side_2 = Input.get_integer_number("Type the 2º side of the triangle: ", must_be_positive=True)
    side_3 = Input.get_integer_number("Type the 3º side of the triangle: ", must_be_positive=True)

    # Step 2: Check if the sides can form a triangle.
    if can_form_a_triangle(side_1, side_2, side_3):
        print(f"Can form a triangle.")
        classify_triangle(side_1, side_2, side_3)
    else:
        print(f"Can't form a triangle.") 


def main() -> None:
    right_triangle_validator()


if __name__ == "__main__":
    main()
