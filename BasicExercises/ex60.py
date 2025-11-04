from utils import Input
from math import hypot


def triangle_hypotenuse_calculator():
	"""
	This program calculate the hypotenuse of a right angled triangle
	Author: Gustavo Assi Alencar.
	Date:   04/11/2025.
	"""

	# Step 1: Get base and height from right angled triangle.
	base = Input.get_float_number(">>> Type the triangle base value: ", must_be_positive=True)
	height = Input.get_float_number(">>>Type the triangle height value: ", must_be_positive=True)

	# Step 2: Calculate hypotenuse.
	hypotenuse = hypot(base, height)

	# Step 3: Display the result.
	print(f">>> hypotenuse: {hypotenuse:.3f}")


def main():
	triangle_hypotenuse_calculator()


if __name__ == "__main__":
	main()
