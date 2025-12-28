import matplotlib.pyplot as plt
from math import sqrt
from pythonproblems.functions.utils import Input


def get_point_coordinates(point: str) -> tuple:
    """
    Get from user the values of x and y coordiantes from a point.
    :param point: the point identifier.
    :return: a tuple with point coordinates (x and y)
    """
    
    x = Input.get_float_number(f"Type the x coordinate of {point}: ") 
    y = Input.get_float_number(f"Type the y coordinate of {point}: ")

    return (x, y)


def lines_are_parallel(P: tuple, Q: tuple, R: tuple, S: tuple):
    """
    Checks if lines PQ and RS are parallel.
    :param P: coordinates of point P.
    :param Q: coordinates of point Q.
    :param R: coordinates of point R.
    :param S: coordinates of point S.
    :return: True if they are parallel, False otherwise.
    """

    dot_product = (Q[0]-P[0])*(R[0]-S[0]) + (Q[1]-P[1])*(R[1]-S[1])
    length_PQ = sqrt((Q[0]-P[0])**2 + (Q[1]-P[1])**2)
    length_SR = sqrt((R[0]-S[0])**2 + (R[1]-S[1])**2)

    return dot_product - length_PQ*length_SR == 0


def display_quadrilateral(P: tuple, Q: tuple, R: tuple, S: tuple) -> None:
    """
    Function to display quadrilateral in screen given it's vertices.
    :param P: coordinates of point P.
    :param Q: coordinates of point Q.
    :param R: coordinates of point R.
    :param S: coordinates of point S.
    """

    vertices = [P, Q, R, S, P]
    x_coords = [v[0] for v in vertices]
    y_coords = [v[1] for v in vertices]

    plt.figure(figsize=(6, 6))
    plt.plot(x_coords, y_coords, marker='o', linestyle='-')
    plt.fill(x_coords, y_coords, alpha=0.3, color='skyblue')
    plt.text(P[0], P[1] + 0.1, 'P', ha='center', color='blue')
    plt.text(Q[0], Q[1] + 0.1, 'Q', ha='center', color='blue')
    plt.text(R[0], R[1] + 0.1, 'R', ha='center', color='blue')
    plt.text(S[0], S[1] + 0.1, 'S', ha='center', color='blue')
    plt.title("Quadrilateral view")
    plt.axis(True)
    plt.grid(True)
    plt.show()


def parallel_lines_tester() -> None:
    """
    This program test whether two lines PQ and RS are parallel. 
    The four points are P(x1, y1), Q(x2, y2), R(x3, y3), S(x4, y4).
    Author: Gustavo Assi Alencar.
    Date:   25/12/2025.
    """

    # Step 1: Get P(x1, y1), Q(x2, y2), R(x3, y3), S(x4, y4).
    P = get_point_coordinates("P")
    Q = get_point_coordinates("Q")
    R = get_point_coordinates("R")
    S = get_point_coordinates("S")


    # Step 2: Check if PQ and RS are parallel using dot-product property.
    if lines_are_parallel(P, Q, R, S):
        print(">>> PARALLEL")
    else:
        print(">>> NOT PARALLEL")

    # Step 3: Display quadrilateral in screen.
    display_quadrilateral(P, Q, R, S)
    

def main() -> None:
    parallel_lines_tester()


if __name__ == "__main__":
    main()
