from utils import Input


def count_four_in_list() -> None:
	"""
	This program counts the number "4" in a given numeric list.
	Author: Gustavo Assi Alencar.
	Date:   30/10/2025.
	"""

	# Step 1: Get the numbers from user and ensure all information is numeric.
	numbers = Input.get_string("Type the numbers (comma-separated): ")
	numbers_list = [number.strip() for number in numbers.split(",")]

	if all([element.isnumeric() for element in numbers_list]):

		# Step 2: Count how many fours.
		amount_of_fours = 0
		for number in numbers_list:
			if number == '4':
				amount_of_fours += 1

		# Alternative solution is: amount_of_fours = numbers_list.count('4')

		# Step 3: Display the result.
		if amount_of_fours == 0:
			print("The list doesn't have any four!")
		elif amount_of_fours == 1:
			print("The list has a unique four!")
		else:
			print(f"The list has exactly {amount_of_fours} fours!")
	
	else:
		print("User didn't input a numeric list!")


def main() -> None:
	count_four_in_list()


if __name__ == "__main__":
	main()