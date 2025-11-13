import os

from utils import Input


def external_command_runner() -> None:
	"""
	This program calls an external command.
	Author: Gustavo Assi Alencar.
	Date:   02/11/2025.
	"""

	# Step 1: Type an command.
	command = Input.get_string("Type a command: ", stripped=True)

	# Step 2: Run the command.
	os.system(command=command)


def main() -> None:
	external_command_runner()


if __name__ == "__main__":
	main()
