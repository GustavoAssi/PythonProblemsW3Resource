from utils import Input


def expression_solver():
	"""
	This program solve (x + y) * (x + y) given x and y values.
	Author: Gustavo Assi Alencar.
	Date:   01/11/2025.
	"""

	# Step 1: Get x and y.
	x = Input.get_float_number("Type value of x: ")
	y = Input.get_float_number("Type value of y: ")

	# Step 2: Evaluate (x + y) * (x + y)
	expression = (x + y) ** 2

	# Step 3: Display result.
	print(f"({x} + {y})² = {expression}")


def main():
	expression_solver()


if __name__ == "__main__":
	main()
