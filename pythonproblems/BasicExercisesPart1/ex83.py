from pythonproblems.functions.utils import Input


def list_greather_than_test() -> None:
	"""
	This program tests whether all numbers in a list are greater than a certain number.
	Author: Gustavo Assi Alencar.
	Date:   08/11/2025.
	"""

	# Step 1: Get the number.
	number = Input.get_float_number("Type any number: ")

	# Step 2: Get a list.
	numbers = Input.get_string("Type a list of numbers: ", stripped=True)
	numbers_list = [int(value.strip()) for value in numbers.split(",") if value.strip().isnumeric()]

	# Step 3: Display results.
	for value in numbers_list:
		if value > number:
			print(f">>> {value}")


def main() -> None:
	list_greather_than_test()


if __name__ == "__main__":
	main()
