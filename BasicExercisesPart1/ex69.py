from utils import Input


def sort_three_numbers() -> None:
	"""
	This program sorts three integers without using conditional statements and loops.
	Author: Gustavo Assi Alencar.
	Date:   05/11/2025.
	"""

	# Step 1: Get the three numbers from user.
	a = Input.get_integer_number("Type the 1º integer: ")
	b = Input.get_integer_number("Type the 2º integer: ")
	c = Input.get_integer_number("Type the 3º integer: ")

	# Step 2: Sort the numbers without conditionals.
	a1 = min(a, b, c)
	a3 = max(a, b, c)
	a2 = (a + b + c) - (a1 + a3)

	# Step 3: Display the three numbers sorted.
	print(f">>> Sorted numbers: ", a1, a2, a3)
	

def main() -> None:
	sort_three_numbers()


if __name__ == "__main__":
	main()
