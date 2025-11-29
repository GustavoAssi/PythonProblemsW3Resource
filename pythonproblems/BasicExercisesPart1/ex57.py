from time import time
from pythonproblems.functions.utils import Input


def sum(a: int, b: int) -> int:
	return a + b


def method_execution_time() -> None:
	"""
	This program gets the execution time of a Python method
	Author: Gustavo Assi Alencar.
	Date:   04/11/2025.
	"""

	begin = time()

	# Step 1: Get two integers.
	a = Input.get_integer_number("Type 1º integer: ")
	b = Input.get_integer_number("Type 2º integer: ")

	# Step 2: Get the sum
	result = sum(a, b)

	# Step 3: Show result
	print(f"{a} + {b} = {result}")

	end = time()
	execution_time = end - begin
	print(f">>> execution time: {execution_time:.3f} s")


def main() -> None:
	method_execution_time()


if __name__ == "__main__":
	main()
