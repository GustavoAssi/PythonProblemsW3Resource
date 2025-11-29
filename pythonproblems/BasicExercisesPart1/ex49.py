import os
import os.path
import subprocess

from pathlib import Path
from pythonproblems.functions.utils import Input


def directory_files_lister() -> None:
	"""
	This program lists all files in a directory.
	Author: Gustavo Assi Alencar.
	Date:   03/11/2025.
	"""

	# Step 1: Pass an existing directory.
	directory = Input.get_string("Input directory path: ", stripped=True)
	user_home = str(Path.home())
	directory = (user_home + "/" + directory) if (user_home not in directory) else directory

	# Step 2: If directory exists, list files using ls (Linux) or dir (Windows).
	if os.path.exists(directory):
		command = ["ls"]
		subprocess.run(command, cwd=directory)


def main() -> None:
	directory_files_lister()


if __name__ == "__main__":
	main()
