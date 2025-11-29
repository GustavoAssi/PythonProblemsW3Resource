from pythonproblems.functions.utils import Input


def string_copy_generator() -> None:
	"""
	This program displays a string that is n copies of a given string.
	Author: Gustavo Assi Alencar.
	Date:   28/10/2025.
	"""

	# Step 1: Get from user a string and the number of copies.
	string = Input.get_string("Type a string to be generated: ")
	copies = Input.get_integer_number("Type the number of copies: ", must_be_positive=True)

	# Step 2: Finish the generation of the copies.
	print(f"{copies * string}")


def main() -> None:
	string_copy_generator()


if __name__ == "__main__":
	main()