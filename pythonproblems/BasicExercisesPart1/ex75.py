import sys


def copyright_information() -> None:
	"""
	This program gets the copyright information and write Copyright information in Python code.
	Author: Gustavo Assi Alencar.
	Date:   06/11/2025.
	"""

	# Step 1: Display copyright information.
	print(sys.copyright)


def main() -> None:
	copyright_information()


if __name__ == "__main__":
	main()
