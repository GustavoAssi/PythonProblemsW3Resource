from pythonproblems.functions.utils import Input


def line_midpoint_calculator() -> None:
	"""
	This program calculates the midpoints of a line.
	Author: Gustavo Assi Alencar.
	Date:   06/11/2025.
	"""
	# Step 1: Get points coordinates.
	x1 = Input.get_float_number(">>> P1 x coordinate value: ")
	y1 = Input.get_float_number(">>> P1 y coordinate value: ")
	x2 = Input.get_float_number(">>> P2 x coordinate value: ")
	y2 = Input.get_float_number(">>> P2 y coordinate value: ")

	# Step 2: Calculate midpoint coordinates.
	x_mid, y_mid = (x1 + x2) / 2, (y1 + y2) / 2

	# Step 3: Show results.
	print(f">>> Midpoint between ({x1}, {y1}) and ({x2}, {y2}) is ({x_mid}, {y_mid})")


def main() -> None:
	line_midpoint_calculator()


if __name__ == "__main__":
	main()
