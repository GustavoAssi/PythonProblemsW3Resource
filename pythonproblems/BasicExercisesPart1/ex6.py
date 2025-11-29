from pythonproblems.functions.utils import Input


def list_and_tuple_generator() -> None:
	"""
	This program takes a sequence of comma-separeted values and creates a list and tuple.
	Author: Gustavo Assi Alencar.
	Date:   26/10/2025.
	"""

	# Step 1: Get the sequence from user.
	sequence = Input.get_string("Type a sequence of values: ")

	# Step 2: Generate list and tuple with values.
	values_list = [value.strip() for value in sequence.split(",")]
	values_tuple = tuple(values_list)

	# Step 3: Display the output.
	print(f"List: {values_list}")
	print(f"Tuple: {values_tuple}")


def main() -> None:
	list_and_tuple_generator()


if __name__ == "__main__":
	main()
