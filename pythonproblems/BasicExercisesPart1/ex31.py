from pythonproblems.functions.utils import Input


def greatest_common_divisor() -> None:
	"""
	This program computes the greatest common divisor of two positive integers.
	Author: Gustavo Assi Alencar.
	Date:   31/10/2025.
	"""
	
	# Step 1: Get the integer numbers.
	a = Input.get_integer_number("Type the 1º integer: ")
	b = Input.get_integer_number("Type the 2º integer: ")
	

	# Step 2: Calculate the GCD using: gcd(a, b) = gcd(b, a % b).
	# When a % b == 0, gcd(x, 0) = x.
	print(f">>> GCD({a}, {b}) = ", end="")
	while a % b != 0:
		a, b = b, a % b

	# Step 3: When the iterations finish, the gcd is b.
	print(b)

	
def main() -> None:
	greatest_common_divisor()


if __name__ == "__main__":
	main()
