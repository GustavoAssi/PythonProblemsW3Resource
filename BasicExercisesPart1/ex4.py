from math import pi
from utils import Input


def circle_area() -> None:
	"""
	This program computes a circle area given a radius.
	Author: Gustavo Assi Alencar.
	Date:   24/10/2025.
	"""
	
	# Step 1: Get from user the radius value.
	radius = Input.get_float_number("Type the radius value: ")

	# Step 2: Compute circle area.
	circle_area = pi * pow(radius, 2)

	# Step 3: Output result.
	print("circle area with radius", radius, "circle area", circle_area)


def main() -> None:
	circle_area()


if __name__ == "__main__":
	main()
