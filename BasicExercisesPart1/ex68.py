from utils import Input


def sum_of_digits() -> None:
	"""
	This program calculates sum of digits of a number
	Author: Gustavo Assi Alencar.
	Date:   05/11/2025.
	"""

	# Step 1: Get the number (integer) from user.
	number = Input.get_integer_number("Type an natural number: ", must_be_positive=True)

	# Step 2: Calculate the sum of digits.
	sum_of_digits = sum([int(digit) for digit in str(number)])

	# Step 3: Display results.
	print(f">>> The sum of digits from inputed number: {sum_of_digits}")


def main() -> None:
	sum_of_digits()


if __name__ == "__main__":
	main()
