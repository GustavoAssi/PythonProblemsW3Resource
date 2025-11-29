import sys


def concatenate_strings() -> None:
	"""
	This program concatenates N strings.
	Author: Gustavo Assi Alencar.
	Date:   08/11/2025.
	"""

	# Step 1: Validate arguments.
	if len(sys.argv) == 1:
		print("Missing strings ...")
		print("Run this program passing arguments like: python3 ex81.py string1 string 2 string3 ... stringn")
	else:
	
		# Step 2: Concatenate strings.
		concatanated_strings = ""
		for string in sys.argv[1:]:
			concatanated_strings += string

		# Step 3: Display results.
		print(f">>> {concatanated_strings}")


def main() -> None:
	concatenate_strings()


if __name__ == "__main__":
	main()
