import os.path

from pathlib import Path
from utils import Input


def file_existence_checker() -> None:
	"""
	This program checks whether a file exists.
	Author: Gustavo Assi Alencar.
	Date:   02/11/2025.
	"""

	# Step 1: Get from user the path from a file.
	user_home = str(Path.home())
	user_file = Input.get_string("Type the file path: ", stripped=True)


	# Step 2: Check if file path exists.
	file_path = (user_home + "/" + user_file) if (user_home not in user_file) else user_file
	if os.path.exists(file_path):
		print(f"File exists in: {file_path}")
	else:
		print(f"Couldn't find file in: {file_path}")


def main() -> None:
	file_existence_checker()


if __name__ == "__main__":
	main()
