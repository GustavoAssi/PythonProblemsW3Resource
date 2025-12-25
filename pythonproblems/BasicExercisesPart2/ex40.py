import matplotlib.pyplot as plt
from pythonproblems.functions.utils import Input


def get_triangle_area(A: tuple, B: tuple, C: tuple) -> float:
    """
    This function computes the value of the area of a triangle.
    :param A: 1º triangle vertix.x
    :param B: 2º triangle vertix.
    :param C: 3º triangle vertix.
    :return: The value of the area of the triangle.
    """

    det = (A[0]*B[1] + C[0]*A[1]+ B[0]*C[1]) - (C[0]*B[1] + A[0]*C[1]+ A[1]*B[0])

    return 0.5 * abs(det)



def is_in_triangle(A: tuple, B: tuple, C: tuple, P: tuple) -> bool:
    """
    This function checks if a point P is in a triangle.
    :param A: 1º triangle vertix.
    :param B: 2º triangle vertix.
    :param C: 3º triangle vertix.
    :param P: a given point.
    :return: True or False
    """

    error = 1e-4

    area_of_ABC = get_triangle_area(A, B, C)
    area_of_ABP = get_triangle_area(A, B, P)
    area_of_ACP = get_triangle_area(A, C, P)
    area_of_BCP = get_triangle_area(B, C, P)

    return abs(area_of_ABC - area_of_ABP - area_of_ACP - area_of_BCP) < error


def display_triangle(A: tuple, B: tuple, C: tuple, P: tuple) -> None:
    """
    This procedure displays a triangle in cartesian coordinates.
    :param A: 1º triangle vertix.
    :param B: 2º triangle vertix.
    :param C: 3º triangle vertix.
    :param P: a given point.
    """

    x = [A[0], B[0], C[0], A[0]] 
    y = [A[1], B[1], C[1], A[1]] 
    plt.plot(x, y, 'b-') 
    plt.fill(x, y, 'skyblue', alpha=0.5)
    plt.scatter(P[0], P[1])
    plt.text(P[0], P[1] + 0.1, 'P', ha='center', color='blue')
    plt.scatter(A[0], A[1])
    plt.text(A[0], A[1] + 0.1, 'A', ha='center', color='blue')
    plt.scatter(B[0], B[1])
    plt.text(B[0], B[1] + 0.1, 'B', ha='center', color='blue')
    plt.scatter(C[0], C[1])
    plt.text(C[0], C[1] + 0.1, 'C', ha='center', color='blue')
    plt.axis('equal')
    plt.grid(True)
    plt.show()


def point_in_triangle() -> None:
    """
    This program checks if a point (x,y) is in a triangle or not. 
    A triangle is formed by three points.
    Author: Gustavo Assi Alencar.
    Date:   23/12/2025.
    """

    # Step 1: Get triangle vertices and point coordinates.
    xa = Input.get_float_number("X coordinate from 1º verix: ")
    ya = Input.get_float_number("Y coordinate from 1º verix: ")
    xb = Input.get_float_number("X coordinate from 2º verix: ")
    yb = Input.get_float_number("Y coordinate from 2º verix: ")
    xc = Input.get_float_number("X coordinate from 3º verix: ")
    yc = Input.get_float_number("Y coordinate from 3º verix: ")
    xp = Input.get_float_number("X coordinate from P: ")
    yp = Input.get_float_number("Y coordinate from P: ")

    A = (xa, ya)
    B = (xb, yb)
    C = (xc, yc)
    P = (xp, yp)

    # Step 2: Check if the point is in the triangle.
    if is_in_triangle(A, B, C, P):
        print(f">>> Point {P} is in the triangle.")
    else:
        print(f">>> Point {P} is not in the triangle.")

    # Step 3: Display the triangle in cartesian plan.
    display_triangle(A, B, C, P)


def main() -> None:
    point_in_triangle()


if __name__ == "__main__":
    main()
