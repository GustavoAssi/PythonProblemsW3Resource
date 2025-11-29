import os

from pythonproblems.functions.utils import Input


def absolute_file_path_finder() -> None:
	"""
	This program gets an absolute file path.
	Author: Gustavo Assi Alencar.
	Date:   04/11/2025.
	"""

	# Step 1: Get file name.
	file_name = Input.get_string("Type file name: ")

	# Step 2: Get file absolute path.
	file_absolute_path = os.path.abspath(file_name)
	
	# Step 3: Display result (if file exists).
	if os.path.exists(file_absolute_path):
		print(f">>> {file_absolute_path}")
	else:
		print(">>> File does not exist.")


def main() -> None:
	absolute_file_path_finder()


if __name__ == "__main__":
	main()
