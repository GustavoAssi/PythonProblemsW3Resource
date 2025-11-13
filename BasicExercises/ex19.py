from utils import Input


def prefix_is_string_modifier() -> None:
	"""
	This program changes a string adding the prefix "Is" in the beginning of the string.
	Author: Gustavo Assi Alencar.
	Date:   28/10/2025.
	"""

	# Step 1: Get a string from user.
	string = Input.get_string("Type a string: ", stripped=True)

	# Step 2: Add the prefix in the string (if necessary).
	if not string.startswith("Is"):
		string = "Is" + string

	# Step 3: Show the result.
	print(string)



def main() -> None:
	prefix_is_string_modifier()


if __name__ == "__main__":
	main()