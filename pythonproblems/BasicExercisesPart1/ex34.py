from pythonproblems.functions.utils import Input


def conditional_sum_to_20() -> None:
	"""
	This program calculates sum two given integers. 
	However: if the sum is between 15 and 20 it will return 20.
	Author: Gustavo Assi Alencar.
	Date:   31/10/2025.
	"""
	
	# Step 1: Get the integers from user.
	i1 = Input.get_integer_number("Type the 1º integer: ")
	i2 = Input.get_integer_number("Type the 2º integer: ")

	# Step 2: Analyse the sum.
	sum = i1 + i2
	if 15 <= sum <= 20:
		sum = 20
	print(f">>> {sum}")


def main() -> None:
	conditional_sum_to_20()


if __name__ == "__main__":
	main()
