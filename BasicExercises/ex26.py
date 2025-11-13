from utils import Input


def list_histogram() -> None:
	"""
	This program creates a histogram from a given list of integers.
	Author: Gustavo Assi Alencar.
	Date:   31/10/2025.
	"""
	
	# Step 1: Set character @.
	character = "@"

	# Step 2: Get list from user.
	list_of_integers = Input.get_string("Type the list of integers (comma-separated): ")
	integers = [int(integer.strip()) for integer in list_of_integers.split(",")]

	# Step 3: Create histogram.
	for integer in integers:
		print(f"{integer * character}")


def main() -> None:
	list_histogram()


if __name__ == "__main__":
	main()