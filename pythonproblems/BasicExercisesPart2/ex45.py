import math as mt
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

from typing import List
from pythonproblems.functions.utils import Input


class Circle:
    def __init__(self, center: tuple, radius: float):
        self.center = center
        self.radius = radius

    def get_intersection(self, other_circle: "Circle") -> List[tuple[float, float]]:
        """
        Returns the intersection from two circles.
        :param other_circle: Another circle to get intersection.
        :return: The intersections in (x, y) format if they exist.
        """

        xc1 = self.center[0]
        yc1 = self.center[1]
        rd1 = self.radius
        xc2 = other_circle.center[0]
        yc2 = other_circle.center[1]
        rd2 = other_circle.radius

        x, y = sp.symbols('x y')
        eq1 = sp.Eq((x - xc1)**2 + (y - yc1)**2, rd1**2) 
        eq2 = sp.Eq((x - xc2)**2 + (y - yc2)**2, rd2**2)
        intersection = sp.solve((eq1, eq2), (x, y))

        return intersection
    
    def get_centers_distance(self, other_circle: "Circle") -> float:
        """
        Returns the distance between the centers from two circles.
        :param other_circle: Another circle to get the distance.
        :return: A float number representing the distance between centers.
        """

        xc1 = self.center[0]
        yc1 = self.center[1]
        xc2 = other_circle.center[0]
        yc2 = other_circle.center[1]
        distance = mt.sqrt((xc1 - xc2)**2 + (yc1 - yc2)**2)

        return distance

    def get_relative_position_between_circles(self, other_circle: "Circle") -> str:
        """
        Returns the relative position between two circles.
        :param other_circle: Another circle to get relative position.
        :return: A string with the relative position.
        """
        
        intersection = self.get_intersection(other_circle=other_circle)
        centers_distance = self.get_centers_distance(other_circle=other_circle)
        if intersection:
            return f">>> Intersection in {intersection}"
        elif centers_distance > self.radius + other_circle.radius:
            return f">>> External circles"
        elif centers_distance == self.radius + other_circle.radius:
            return f">>> Tangent circles"
        elif centers_distance == abs(self.radius - other_circle.radius):
            return f">>> Internal tangent circles"
        elif abs(self.radius - other_circle.radius) < centers_distance < self.radius + other_circle.radius:
            return f">>> Secant circles"
        elif 0 <= centers_distance < abs(self.radius - other_circle.radius):
            return f">>> Internal circles"
        elif centers_distance == 0:
            return f">>> Concentric circles" 


def display_circles(circle_1: Circle, circle_2: Circle, title: str) -> None:
    """
    Procedure to display two circles in 2D-plan.
    :param circle_1: 1º circle.
    :param circle_2: 2º circle.
    """
    xc1 = circle_1.center[0]
    yc1 = circle_1.center[1]
    xc2 = circle_2.center[0]
    yc2 = circle_2.center[1]
    rd1 = circle_1.radius
    rd2 = circle_2.radius
    theta = np.linspace(0, 2 * np.pi, 200)
    x1 = xc1 + rd1 * np.cos(theta)
    y1 = yc1 + rd1 * np.sin(theta)
    x2 = xc2 + rd2 * np.cos(theta)
    y2 = yc2 + rd2 * np.sin(theta)

    plt.figure(figsize=(6, 6))
    plt.title(title)
    plt.plot(x1, y1, label="Circle 1")
    plt.plot(x2, y2, label="Circle 2")

    intersection = circle_1.get_intersection(other_circle=circle_2)
    if intersection:
        for (x, y) in intersection:
            plt.scatter(x, y)

    plt.axhline(0, color="black", linewidth=0.5) 
    plt.axvline(0, color="black", linewidth=0.5)  
    plt.gca().set_aspect('equal') 
    plt.grid(True)
    plt.legend(loc="upper right") 
    plt.show()


def circle_overleap_checker() -> None:
    """
    There are two circles C1 with radius r1, central coordinate (x1, y1) and 
    C2 with radius r2 and central coordinate (x2, y2).
    This program checks if there is a intersection between the circles.
    Author: Gustavo Assi Alencar.
    Date:   25/12/2025.
    """

    # Step 1: Get circles data.
    xc1 = Input.get_float_number("Input x coordinate from 1º circle: ")
    yc1 = Input.get_float_number("Input y coordinate from 1º circle: ")
    rd1 = Input.get_float_number("Input radius value from 1º circle: ")
    print("\n")
    xc2 = Input.get_float_number("Input x coordinate from 2º circle: ")
    yc2 = Input.get_float_number("Input y coordinate from 2º circle: ")
    rd2 = Input.get_float_number("Input radius value from 2º circle: ")

    # Step 2: Analyse relative position between the circles.
    circle_1 = Circle(center=(xc1, yc1), radius=rd1)
    circle_2 = Circle(center=(xc2, yc2), radius=rd2)
    position = circle_1.get_relative_position_between_circles(other_circle=circle_2)
    print(position)
    
    # Step 3: Display the circles.
    display_circles(circle_1=circle_1, circle_2=circle_2, title=position)


def main() -> None:
    circle_overleap_checker()


if __name__ == "__main__":
    main()
