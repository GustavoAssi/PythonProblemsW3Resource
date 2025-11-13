from utils import Input


def difference_from_17() -> None:
	"""
	This program calculates difference between a given number from 17.
	If the number is greater than 17, display twice the absolute difference.
	Author: Gustavo Assi Alencar.
	Date:   27/10/2025.
	"""

	# Step 1: Get a number from user.
	number = Input.get_integer_number("Type an integer number: ")

	# Step 2: Evaluate the result.
	result = 2 * abs(number - 17) if number > 17 else number - 17

	# Step 3: Display the result.
	print(f">>> Result: {result}")


def main() -> None:
	difference_from_17()


if __name__ == "__main__":
	main()