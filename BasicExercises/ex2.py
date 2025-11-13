from os import system
from platform import python_version


def show_python_version() -> None:
	"""
	This program shows the current Python version installed.
	Author: Gustavo Assi Alencar.
	Date:   24/10/2025.
	"""

	# Using system to run python3 --version
	system("python3 --version")

	# Using platform module to get Python version
	py_version = python_version()
	print("Get the Python version by platform module:", py_version)
	

def main() -> None:
	show_python_version()


if __name__ == "__main__":
	main()
