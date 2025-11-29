from pythonproblems.functions.utils import Input


def is_numeric_string(string: str) -> bool:
	"""
	Checks if the string represents a number.

	:param:  string that will be tested.
	:return: True or False.
	"""

	return all([digit.isnumeric() or digit in ".," for digit in string])


def can_be_float_number(numeric_string: str) -> bool:
	"""
	Checks if a numeric string is a float number.

	:param:  string that will be tested.
	:return: True or False.
	"""

	return any([digit in ",." for digit in numeric_string])


def string_to_numeric_parser() -> None:
	"""
	This program parses a string to float or integer.
	Author: Gustavo Assi Alencar.
	Date:   03/11/2025.
	"""

	# Step 1: Get the string from user.
	string = Input.get_string("Type something: ", stripped=True)

	# Step 2: Try to convert string to float or integer according to the string pattern.
	if is_numeric_string(string):
		if can_be_float_number(string):
			string = string.replace(",", ".")
			print(f">>> Converted float value: {float(string)}")
		else:
			print(f">>> Converted int value: {int(string)}")
	else:
		print(f">>> User typed a non numeric string.")


def main() -> None:
	string_to_numeric_parser()


if __name__ == "__main__":
	main()
