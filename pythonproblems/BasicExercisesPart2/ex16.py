from math import sqrt
from pythonproblems.functions.utils import Input


def apply_filter(value: str):
    """
    Apply a filter for a value.
    If value is X as string, then keeps X.
    Otherwise, if is a float number, convert the float number.
    If value is a negative number, fix the signal.
    """
    try:
        new_value = float(value)
        if new_value < 0:
            new_value *= -1
        return new_value
    except ValueError:
        return value.upper()


def has_valid_sides(sides: list) -> bool:
    """
    Returns True if the sides of the triangle has
    valid values for the problem. Otherwise, returns False.
    """

    # Restriction 1: Values only can be equal to X or a float number.
    for value in sides:
        if not (value == 'X' or 'float' in str(type(value))):
            print(">>> [WARNING] Some of the variables are not equal to X!")
            return False

    # Restriction 2: The hypotenuse can't be equal to any of the sides.
    if sides[2] == sides[0] or sides[2] == sides[1]:
        print(">>> [WARNING] One of the sides has equal values with the hipotenuse!")
        return False

    # Restriction 3: If all values are equal to 'X', Pythagoras theorem won't work!
    if sides[0] == sides[1] == sides[2]:
        print(">>> [WARNING] Unable to use Pythagoras theorem with the 3 values as variables!")
        return False

    return True


def right_triangle_third_side() -> None:
    """
    This program gets the third side of a right-angled triangle from two given sides.
    Author: Gustavo Assi Alencar.
    Date:   29/11/2025.
    """

    print("-" * 30)
    print("PYTHAGORAS THEOREM SOLVER".center(30))
    print("-" * 30)

    # Step 1: Get from user the sides of the triangle.
    opposite_side = Input.get_string("Input the opposite side (use 'X' for variable): ", stripped=True)
    adjacent_side = Input.get_string("Input the adjacent side (use 'X' for variable): ", stripped=True)
    hypotenuse = Input.get_string("Input the hypotenuse value (use 'X' for variable): ", stripped=True)
    sides = [apply_filter(value) for value in [opposite_side, adjacent_side, hypotenuse]]

    # Step 2: Get value from sides by Pythagoras formula.
    if has_valid_sides(sides):
        if sides[0] == sides[1] == 'X':
            print(f"The opposite and adjacent side of this triangle are: {sides[2] / sqrt(2)}")
        elif sides[0] == 'X':
            print(f"The opposite side of this triangle is: {sqrt(sides[2]**2 - sides[1]**2)}")
        elif sides[1] == 'X':
            print(f"The adjacent side of this triangle is: {sqrt(sides[2]**2 - sides[0]**2)}")
        elif sides[2] == 'X':
            print(f"The hypotenuse of this triangle is: {sqrt(sides[0]**2 + sides[1]**2)}")
        else:
            if sides[0]**2 + sides[1]**2 == sides[2]**2:
                print("You know the answer!")
            else:
                print("The sides of this triangle does not satisfies the Pythagoras theorem")
    else:
        print("Try again...")


def main() -> None:
    right_triangle_third_side()


if __name__ == "__main__":
    main()
