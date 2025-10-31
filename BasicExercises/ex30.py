from utils import Input


def triangle_area():
	"""
	This program will accept the base and height of a triangle and compute its area.
	Author: Gustavo Assi Alencar.
	Date:   31/10/2025."
	"""
	
	# Step 1: Get the triangle measures, base and height.
	base = Input.get_float_number("Type triangle's base measure: ", must_be_positive=True)
	height = Input.get_float_number("Type triangle's height measure: ", must_be_positive=True)

	# Step 2: Calculate area.
	area = base * height / 2

	# Step 3: Display the result.
	print(f">>> area: {area}")


def main():
	triangle_area()


if __name__ == "__main__":
	main()