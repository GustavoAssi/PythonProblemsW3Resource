from utils import Input


def triple_sum_calculator()-> None:
	"""
	This program calculates the sum of three given numbers. 
	If the values are equal, return three times their sum.
	Author: Gustavo Assi Alencar.
	Date:   29/10/2025.
	"""

	# Step 1: Get the numbers from user.
	number_1 = Input.get_float_number("Type the 1º number: ")
	number_2 = Input.get_float_number("Type the 2º number: ")
	number_3 = Input.get_float_number("Type the 3º number: ")

	# Step 2: Calculate the sum.
	sum = number_1 + number_2 + number_3

	# Step 3: Display the result.
	print(f">>> Sum: {sum}")


def main() -> None:
	triple_sum_calculator()


if __name__ == "__main__":
	main()