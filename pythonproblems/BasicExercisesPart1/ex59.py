from pythonproblems.functions.utils import Input


def height_in_centimeters() -> None:
	"""
	This program converts height (in feet and inches) to centimeters
	Author: Gustavo Assi Alencar.
	Date:   04/11/2025.
	"""

	# Step 1: Input user height in feet and inches.
	print("Input your height in feet and inches.")
	feet = Input.get_integer_number(">>> feet: ", must_be_positive=True)
	inches = Input.get_integer_number(">>> inches: ", must_be_positive=True)

	# Step 2: Convert to centimeters.
	height_in_centimeters = feet * 30.48 + inches * 2.54

	# Step 3: Display height in centimeters.
	print(f">>> Your height (cm): {height_in_centimeters}")


def main() -> None:
	height_in_centimeters()


if __name__ == "__main__":
	main()

