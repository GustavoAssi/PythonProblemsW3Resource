import sys


def command_line_arguments() -> None:
	"""
	This program gets the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
	Author: Gustavo Assi Alencar.
	Date:   08/11/2025.
	"""

	# Step 1: Display script name.
	print(f">>> Script name: {sys.argv[0]}")

	# Step 2: Display number of arguments.
	print(f">>> Number of arguments: {len(sys.argv)}")
	
	# Step 3: Display arguments.
	print(f">>> Arguments list: {sys.argv}")


def main() -> None:
	command_line_arguments()


if __name__ == "__main__":
	main()
