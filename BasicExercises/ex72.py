import math


from utils import Input


def math_module_details() -> None:
	"""
	This program gets the details of the math module.
	Author: Gustavo Assi Alencar.
	Date:   06/11/2025.
	"""

	# Step 1: Display math module functions attributes (object).
	print("All math functions and atributes.")
	math_module_objects = dir(math)
	for object in math_module_objects:
		print(f">>> {object}")

	# Step 2: Ask for user to use help from one of the given objects list.
	user_query = Input.get_string("Type an object to get more informations: ", stripped=True)
	if user_query in math_module_objects:
		exec(f"help(math.{user_query})")
	else:
		print(f'Couldn\'t find "{user_query}" defined in math module.')


def main() -> None:
	math_module_details()


if __name__ == "__main__":
	main()
