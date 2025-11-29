from pythonproblems.functions.utils import Input


def list_to_string_concatenator() -> None:
	"""
	This program concatenates all elements in a list into a string and returns it.
	Author: Gustavo Assi Alencar.
	Date:   31/10/2025.
	"""
	
	# Step 1: Get the list from user.
	user_list = Input.get_string("Type the list elements (comma-separated): ")
	elements = [element.strip() for element in user_list.split(",")]

	# Step 2: Concatenate all elements.
	output_string = ""
	for element in elements:
		output_string += element

	# Alternative: sum(elements)

	# Step 3: Display output string
	print(f">>> List: {elements}")
	print(f">>> Concatenated string: {output_string}")


def main() -> None:
	list_to_string_concatenator()


if __name__ == "__main__":
	main()
