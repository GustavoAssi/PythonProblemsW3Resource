from pythonproblems.functions.utils import Input


def print_without_newline() -> None:
	"""
	This program prints without a newline or space.
	Author: Gustavo Assi Alencar.
	Date:   03/11/2025.
	"""

	# Step 1: get a positive value from user
	value = Input.get_integer_number("Type a positive value: ", must_be_positive=True)

	# Step 2: print a newline.
	for _ in range(0, value):
		print('*', end="")
	print("\n")


def main() -> None:
	print_without_newline()


if __name__ == "__main__":
	main()
