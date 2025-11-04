import os


def file_path_and_name_finder():
	"""
	This program retrieve the path and name of the file currently being executed.
	Author: Gustavo Assi Alencar.
	Date:   03/11/2025.
	"""

	# Step 1: Get current file name using os module.
	current_file = __file__
	current_file_path = os.path.realpath(current_file)

	# Step 2: Display Informations.
	print(f">>> current file: {current_file}")
	print(f">>> current file path: {current_file_path}")


def main():
	file_path_and_name_finder()


if __name__ == "__main__":
	main()
