from pythonproblems.functions.utils import Input


def personal_info_formatter() -> None:
	"""
	This program displays your name, age, and address on three different lines.
	Author: Gustavo Assi Alencar.
	Date:   01/11/2025.
	"""

	# Step 1: Get the data from user.
	name = Input.get_string("Type your name: ")
	age = Input.get_integer_number("Type your age: ", must_be_positive=True)
	address = Input.get_string("Type your address: ")

	# Step 2: Display the information.
	print(f">>> name: {name}")
	print(f">>> age: {age} years old")
	print(f">>> address: {address}")


def main() -> None:
	personal_info_formatter()


if __name__ == "__main__":
	main()
