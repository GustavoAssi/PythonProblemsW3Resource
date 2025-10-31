from utils import Input


def string_prefix_copies():
	"""
	This program get n (non-negative integer) copies of the first 2 characters of a given string.
	Author: Gustavo Assi Alencar.
	Date:   30/10/2025.
	"""

	# Step 1: Get string and number of copies from user.
	string = Input.get_string("Type a string: ", stripped=True)
	number_of_copies = Input.get_integer_number("Number of copies: ", must_be_positive=True)

	# Step 2: Display the copies.
	result = number_of_copies * string[:2]
	print(f">>> {result}") 


def main():
	string_prefix_copies()


if __name__ == "__main__":
	main()