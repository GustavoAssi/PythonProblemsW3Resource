import matplotlib.pyplot as plt
import numpy as np

from math import sqrt
from pythonproblems.functions.utils import Input


def display_circle(xc: float, yc: float, r: float, p1: tuple, p2: tuple, p3: tuple) -> None:
    """
    Procedure to draw a circle using matplotlib functions.
    :param xc: x coordinate from center.
    :param yc: y coordinate from center.
    :param r: circle radius.
    :param p1: 1º point.
    :param p2: 2º point.
    :param p3: 3º point.
    """
    
    theta = np.linspace(0, 2 * np.pi, 200)
    x = xc + r * np.cos(theta)
    y = yc + r * np.sin(theta)

    plt.figure(figsize=(6, 6))
    plt.title(f"C: (x - {xc})² + (y - {yc})² = ({r})²")
    plt.plot(x, y, label="Circle")
    plt.scatter(xc, yc, label="Center")
    plt.scatter(p1[0], p1[1], label="P1")
    plt.scatter(p2[0], p2[1], label="P2")
    plt.scatter(p3[0], p3[1], label="P3")
    plt.axhline(0, color="black", linewidth=0.5) 
    plt.axvline(0, color="black", linewidth=0.5)  
    plt.gca().set_aspect('equal') 
    plt.grid(True)
    plt.legend(loc="upper right") 
    plt.show()


def circle_from_three_points() -> None:
    """
    This program computes the radius and the central coordinate (x, y) of a 
    circle which is constructed from three given points on the plane surface.
    Author: Gustavo Assi Alencar.
    Date:   23/12/2025.
    """

    # Step 1: Get the three points coordinates from user.
    x1 = Input.get_integer_number("Value of x1 (integer value): ")
    y1 = Input.get_integer_number("Value of y1 (integer value): ")
    print("")
    x2 = Input.get_integer_number("Value of x2 (integer value): ")
    y2 = Input.get_integer_number("Value of y2 (integer value): ")
    print("")
    x3 = Input.get_integer_number("Value of x3 (integer value): ")
    y3 = Input.get_integer_number("Value of y3 (integer value): ")
    print("")

    # Step 2: Find the value of xc, yc and R.
    A = 2 * (x2 - x1)
    B = 2 * (y2 - y1)
    D = 2 * (x3 - x1)
    E = 2 * (y3 - y1)
    C = (x2**2 + y2**2) - (x1**2 + y1**2)
    F = (x3**2 + y3**2) - (x1**2 + y1**2)

    if B*D - A*E == 0:
        print("The given coordinates can't be part of a circle.")
    else:
        xc = round((B*F - C*E) / (B*D - A*E), 3)
        yc = round((C*D - A*F) / (B*D - A*E), 3)
        r = round(sqrt((x1 - xc)**2 + (y1 - yc)**2), 3)

        print(f">>> Circle center: ({xc}, {yc})")
        print(f">>> Circle radius: {r}")

        # Step 3: Display the circle using matplotlib.
        display_circle(xc, yc, r, (x1, y1), (x2, y2), (x3, y3))


def main() -> None:
    circle_from_three_points()


if __name__ == "__main__":
    main()
