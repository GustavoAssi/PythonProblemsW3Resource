from utils import Input


def least_common_multiple() -> None:
	"""
	This program computes least common multiple of two positive integers.
	Author: Gustavo Assi Alencar.
	Date:   31/10/2025.
	"""
	
	# Step 1: Get the integer numbers.
	a = Input.get_integer_number("Type the 1º integer: ")
	b = Input.get_integer_number("Type the 2º integer: ")
	p = a * b

	# Step 2: Calculate LCM: the LCM = abs(a * b) / GCD(a, b).
	print(f">>> LCM({a}, {b}) = ", end="")
	while a % b != 0:
		a, b = b, a % b
	
	# Step 3: Display result, remember that current value of b is the GCD(a, b).
	print(f"{abs(p) / b}")


def main() -> None:
	least_common_multiple()


if __name__ == "__main__":
	main()
