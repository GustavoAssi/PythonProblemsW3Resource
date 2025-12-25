import os
from pythonproblems.functions.utils import Input


def display_system(a, b, c, d, e, f) -> None:
    """
    Procedure to display the system of equations.
    :param a: x coeficient from 1ª equation.
    :param b: y coeficient from 1ª equation.
    :param c: independet term from 1ª equation.
    :param d: x coeficient from 2ª equation.
    :param e: y coeficient from 2ª equation.
    :param f: independent term from 2ª equation.
    """
    print("\n")
    print(f"{a}x + {b}y = {c}")
    print(f"{d}x + {e}y = {f}")
    print("\n")


def solve_linear_equations() -> None:
    """
    This program solves a 2x2 system of equations.
    ax+by=c
    dx+ey=f
    Where a, b, c, d, e and f are given.
    Author: Gustavo Assi Alencar.
    Date:   23/12/2025.
    """

    print(30 * "=")
    print("SYSTEM SOLVER".center(30))
    print("ax + by = c")
    print("dx + ey = f")
    print(30 * "=")

    # Step 1: Get the values of a, b, c, d, e and f from user.
    a = Input.get_integer_number("Type the value of a: ")
    b = Input.get_integer_number("Type the value of b: ")
    c = Input.get_integer_number("Type the value of c: ")
    d = Input.get_integer_number("Type the value of d: ")
    e = Input.get_integer_number("Type the value of e: ")
    f = Input.get_integer_number("Type the value of f: ")

    os.system("clear")
    display_system(a, b, c, d, e, f)

    # Step 2: Compute the values of x and y if the system has solutions.
    if b*d - a*e == 0:
        print(f"There is no solution for this system.")
    else:
        x = (b*f - c*e) / (b*d - a*e)
        y = (c*d - a*f) / (b*d - a*e)
        print(f">>> x = {x}")
        print(f">>> y = {y}")


def main() -> None:
    solve_linear_equations()


if __name__ == "__main__":
    main()
