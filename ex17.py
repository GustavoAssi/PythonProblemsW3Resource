def number_range_tester():
	"""
	This program test whether a number is within 100 of 1000 or 2000.
	Author: Gustavo Assi Alencar.
	Date:   28/10/2025.
	"""

	# Step 1: Get the number from user.
	number = int(input("Type a number: "))

	# Step 2: Verify the condition.
	if abs(1000 - number) <= 100 or abs(2000 - number) <= 100:
		print("Number is within 100 of 1000 or 2000.")
	else:
		print("Number is not within 100 of 1000 or 2000.")


def main():
	number_range_tester()


if __name__ == "__main__":
	main()
