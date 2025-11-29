from pythonproblems.functions.utils import Input


def file_extension_extractor() -> None:
	"""
	This program displays the extension from a file.
	Author: Gustavo Assi Alencar.
	Date:   26/10/2025.
	"""

	# Step 1: Get file name from user. 	
	file_name = Input.get_string("Type file name: ")

	# Step 2: Validate the file name (just 1 dot).
	amount_of_dots = file_name.count(".")
	if amount_of_dots == 1:

		# Step 3: Since is a valid file, get the extension.
		dot_index = file_name.index(".")
		extension_name = file_name[dot_index + 1:]
		print(f"Extension: {extension_name}")

	elif amount_of_dots == 0:
		print("Invalid file name!")
		print("Couldn't find any extension on the file name.")
	else:
		print("Invalid file name!")
		print("File has more than 1 dot!")


def main() -> None:
	file_extension_extractor()


if __name__ == "__main__":
	main()
