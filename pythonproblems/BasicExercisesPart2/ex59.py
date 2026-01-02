import matplotlib.pyplot as plt
from math import atan2
from pythonproblems.functions.utils import Input


def order_vertices(vertices: list[tuple]) -> list[tuple]:
    """
    Sort the sequence of vertices from a convex polygon.
    :param vertices: the list of vertices from polygon.
    :return: the same list with vertices sorted.
    """
    cx = sum(x for x, _ in vertices) / len(vertices)
    cy = sum(y for _, y in vertices) / len(vertices)
    vertices_angles = [
        (x, y, atan2(y - cy, x - cx)) for x, y in vertices
    ]

    vertices_sorted = sorted(vertices_angles, key=lambda vertix: vertix[2])

    return [(x, y) for x, y, _ in vertices_sorted]


def get_area_of_triangle(vertex_1: tuple[float, float], vertex_2: tuple[float, float], vertex_3: tuple[float, float]) -> float:
    """
    Returns the area of triangle formed by its vertices.
    :param vertex_1: 1º vertex from triangle.
    :param vertex_2: 2º vertex from triangle.
    :param vertex_3: 3º vertex from triangle.
    :return: Float number that represents the area of the triangle.
    """
    x1, y1 = vertex_1
    x2, y2 = vertex_2
    x3, y3 = vertex_3
    det = (x1*y2 + y1*x3 + x2*y3) - (x3*y2 + x1*y3 + x2*y1)

    return 0.5 * abs(det)


def display_polygon_with_area(vertices: list[tuple]) -> None:
    """
    Display in 2D plane the polygon formed by a list of vertices.
    """
    for vertex in vertices:
        plt.scatter(*vertex)
    plt.grid(True)
    plt.show()


def convex_polygon_area() -> None:
    """
    This program computes the area of a convex polygon.
    The vertices have the names vertex 1, vertex 2, vertex 3, ... vertex n according to the order of edge connections.
    Where each vertex has his own coordinate (x, y) in the plane.
    Author: Gustavo Assi Alencar.
    Date:   28/12/2025.
    """

    # Step 1: Get polygon vertices, according the number of vertices.
    vertices = []
    number_of_vertices = Input.get_integer_number("Input number of vertices: ", must_be_positive=True)
    for index in range(number_of_vertices):
        x = Input.get_float_number(f"X coordinate from {index + 1}º vertex: ")
        y = Input.get_float_number(f"Y coordinate from {index + 1}º vertex: ")
        print("")
        vertix = (x, y)
        vertices.append(vertix)

    if number_of_vertices >= 3:

        # Step 2: Divide polygons into triangles and sum the areas from all triangles.
        ordered_vertices = order_vertices(vertices)
        total_area = 0
        vertex_1 = ordered_vertices.pop(0)
        for index in range(0, len(ordered_vertices) - 1):
            vertex_2 = ordered_vertices[index]
            vertex_3 = ordered_vertices[index + 1]
            total_area += get_area_of_triangle(vertex_1, vertex_2, vertex_3)

        print(f">>> Area of polygon formed by {vertices}: {total_area}")
        display_polygon_with_area([vertex_1] + vertices)

    else:
        print(f"The number of vertices must be equal o greater than 3 to form a polygon.")



def main() -> None:
    convex_polygon_area()


if __name__ == "__main__":
    main()
