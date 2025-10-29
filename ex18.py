def string_copy_generator():
	"""
	Write a Python program that returns a string that is n copies of a given string.
	Author: Gustavo Assi Alencar.
	Date:   28/10/2025.
	"""

	# Step 1: Get from user a string and the number of copies.
	string = input("Type a string to be generated: ")
	n = int(input("Number of copies: "))

	# Step 2: Finish the generation of the copies.
	print(f"{n * string}")


def main():
	string_copy_generator()


if __name__ == "__main__":
	main()