import os.path, time


from pythonproblems.functions.utils import Input


def file_timestamps() -> None:
	"""
	This program retrieves the date and time of file creation and modification.
	Author: Gustavo Assi Alencar.
	Date:   04/11/2025.
	"""

	# Step 1: Get file name.
	file_name = Input.get_string("Type file name: ")

	# Step 2: Get file absolute path.
	file_absolute_path = os.path.abspath(file_name)
	
	# Step 3: If file exists, get 'Last modified' and 'Create' date and time.
	if os.path.exists(file_absolute_path):
		print(f"Created: {time.ctime(os.path.getmtime(file_absolute_path))}")
		print(f"Last Modified: {time.ctime(os.path.getctime(file_absolute_path))}")
	else:
		print(">>> File does not exist.")


def main() -> None:
	file_timestamps()


if __name__ == "__main__":
	main()
