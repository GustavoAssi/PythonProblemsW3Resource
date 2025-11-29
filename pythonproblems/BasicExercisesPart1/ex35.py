from pythonproblems.functions.utils import Input


def equality_five_checker() -> None:
	"""
	This program displays true if the two given integer values are equal or their sum or difference is 5.
	Author: Gustavo Assi Alencar.
	Date:   31/10/2025.
	"""
	
	# Step 1: Get the integers from user.
	i1 = Input.get_integer_number("Type the 1º integer: ")
	i2 = Input.get_integer_number("Type the 2º integer: ")

	# Step 2: Validate the condition.
	if i1 == i2 or i1 + i2 == 5 or abs(i1 - i2) == 5:
		print(">>> TRUE")
	else:
		print(">>> FALSE")


def main() -> None:
	equality_five_checker()


if __name__ == "__main__":
	main()
