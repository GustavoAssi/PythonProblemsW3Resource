import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Arc
from pythonproblems.functions.utils import Input


class Vector:
    def __init__(self, origin: tuple[float, float] = (0, 0), destiny: tuple[float, float] = (0, 0)):
        self.__origin = origin
        self.__destiny = destiny
        self.__x_component = destiny[0] - origin[0]
        self.__y_component = destiny[1] - origin[1]
        self.__length = np.sqrt((origin[0] - destiny[0])**2 + (origin[1] - destiny[1])**2)

    @property
    def get_origin(self) -> tuple[float, float]:
        return self.__origin
    
    @property
    def get_destiny(self) -> tuple[float, float]:
        return self.__destiny
    
    @property
    def get_x_component(self) -> float:
        return self.__x_component
    
    @property
    def get_y_component(self) -> float:
        return self.__y_component
    
    @property
    def get_components(self) -> tuple[float, float]:
        return (self.__x_component, self.__y_component)

    @property
    def get_length(self):
        return self.__length
    
    def algebric_representation(self) -> str:
        return f"({self.__x_component})î + ({self.__y_component})ĵ"
    
    def get_dot_product_between(self, other_vector: "Vector") -> float:
        x_u = self.__x_component
        y_u = self.__y_component
        x_v = other_vector.get_x_component
        y_v = other_vector.get_y_component

        return x_u*x_v + y_u*y_v
    
    def get_angle_between(self, other_vector: "Vector") -> float:
        dot_product = self.get_dot_product_between(other_vector)
        u_length = self.get_length
        v_length = other_vector.get_length
        angle_radians = np.arccos((dot_product / (u_length * v_length)))

        return angle_radians
    
    def is_ortogonal_with(self, other_vector: "Vector") -> bool:
        return self.get_dot_product_between(other_vector) == 0
    

def display_vectors(u: Vector, v: Vector) -> None:
    """
    Procedure to display two vectors in 2D plane.
    :param u: 1º vector.
    :param v: 2º vector.
    """

    u_translated = Vector((0, 0), (u.get_x_component, u.get_y_component)) 
    v_translated = Vector((0, 0), (v.get_x_component, v.get_y_component))

    ax = plt.subplots(figsize=(6, 6))[1] 
    ax.quiver(*u_translated.get_origin, *u_translated.get_components, angles='xy', scale_units='xy', scale=1, color='red', label='u') 
    ax.quiver(*v_translated.get_origin, *v_translated.get_components, angles='xy', scale_units='xy', scale=1, color='blue', label='v')
    angle_u = np.degrees(np.arctan2(u.get_y_component, u.get_x_component))
    angle_v = np.degrees(np.arctan2(v.get_y_component, v.get_x_component))
    angle_u = angle_u % 360
    angle_v = angle_v % 360
    delta = (angle_v - angle_u) % 360
    if delta > 180:
        theta1 = angle_v
        theta2 = angle_u + 360
    else:
        theta1 = angle_u
        theta2 = angle_v
    arc = Arc((0, 0), 1, 1, angle=0, theta1=theta1, theta2=theta2, color='green')
    ax.add_patch(arc)
    ax.text(u_translated.get_origin[0] + 0.6, u_translated.get_origin[1] + 0.2, f"{np.degrees(u.get_angle_between(v)):.1f}°", color='green')
    d = u_translated.get_length
    ax.set_xlim(min(u_translated.get_origin[0], v_translated.get_origin[0]) - d, max(u_translated.get_destiny[0], v_translated.get_destiny[0]) + d) 
    ax.set_ylim(min(u_translated.get_origin[1], v_translated.get_origin[1]) - d, max(u_translated.get_destiny[1], v_translated.get_destiny[1]) + d) 
    ax.set_aspect('equal') 
    ax.set_xlabel('X') 
    ax.set_ylabel('Y') 
    ax.grid(True) 
    ax.legend() 
    plt.show()


def ortogonal_line_checker() -> None:
    """
    There are four different points on a plane, 
    A(xa,ya), B(xb, yb), C(xc, yc) and D(xd, yd).
    This program determines whether AB and CD are orthogonal.
    Author: Gustavo Assi Alencar.
    Date:   28/12/2025.
    """

    # Step 1: Create vectors u = AB and v = CD.
    A = (
        Input.get_float_number("Input x coordinate from point A (float number): "), 
        Input.get_float_number("Input x coordinate from point A (float number): ")
        )
    B = (
        Input.get_float_number("Input x coordinate from point B (float number): "), 
        Input.get_float_number("Input x coordinate from point B (float number): ")
        )
    C = (
        Input.get_float_number("Input x coordinate from point C (float number): "), 
        Input.get_float_number("Input x coordinate from point C (float number): ")
        )
    D = (
        Input.get_float_number("Input x coordinate from point D (float number): "), 
        Input.get_float_number("Input x coordinate from point D (float number): ")
        )
    u = Vector(A, B)
    v = Vector(C, D)

    print(">>> u =", u.algebric_representation())
    print(">>> v =", v.algebric_representation())

    # Step 2: Check if u and v are ortogonal vectors.
    if u.is_ortogonal_with(v):
        print(">>> Ortogonal vectors!")
    else:
        print(">>> Not ortogonal vectors!")

    # Step 3: Display vectors in 2D plane.
    display_vectors(u, v)


def main() -> None:
    ortogonal_line_checker()


if __name__ == "__main__":
    main()
