from utils import Input


def number_expansion_calculator() -> None:
	"""
	This program recieves an integer number (n) and display the value of n + n² + n³.
	Author: Gustavo Assi Alencar.
	Date:   27/10/2025. 
	"""

	# Step 1: Get the number from user.
	n = Input.get_integer_number("Type an integer number: ")

	# Step 2: Evaluate the expansion n + n² + n³
	result = n + pow(n, 2) + pow(n, 3)

	# Step 3: Show the result.
	print(f"Result: {result}")


def main() -> None:
	number_expansion_calculator()


if __name__ == "__main__":
	main()