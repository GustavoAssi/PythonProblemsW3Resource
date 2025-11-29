import os


from pythonproblems.functions.utils import Input


def file_or_directory_checker() -> None:
	"""
	This program checks whether a file path is a file or a directory.
	Author: Gustavo Assi Alencar.
	Date:   08/11/2025.
	"""

	# Step 1: Get a path.
	path = Input.get_string("Type a path: ", stripped=True)

	# Step 2: Check if is a directory, file or special file (if path exists).
	if os.path.exists(path):
		if os.path.isdir(path):
			print(">>> Is a directory")
		elif os.path.isfile(path):
			print(">>> Is a file")
		else:
			print(">>> Is a special file (socket, FIFO, device file)")
	else:
		print(f"Couldn't found path: {path}")


def main() -> None:
	file_or_directory_checker()


if __name__ == "__main__":
	main()
