from pythonproblems.functions.utils import Input


def even_odd_checker() -> None:
	"""
	This program determines whether a given number is even or odd.
	Author: Gustavo Assi Alencar.
	Date:   30/10/2025.
	"""

	# Step 1: Get the number from user.
	number = Input.get_integer_number("Type an integer number: ")
	
	# Step 2: Check if is even or odd.
	if number % 2 == 0:
		print("Number is even")
	else:
		print("Number is odd")


def main() -> None:
	even_odd_checker()


if __name__ == "__main__":
	main()