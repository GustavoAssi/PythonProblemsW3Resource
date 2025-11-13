import cProfile
from utils import Input


def sum_of_integers(a: int, b: int) -> int:
	"""
	Returns the sum from two integers a and b.

	:param a: 1º integer.
	:param b: 2º integer.
	:return: a + b.
	"""

	return a + b


def program_profiler() -> None:
	"""
	This program determines the profiling of Python programs.
	Author: Gustavo Assi Alencar.
	Date:   04/11/2025.
	"""

	# Step 1: Get two integer numbers.
	a = Input.get_integer_number("Type the 1º integer: ")
	b = Input.get_integer_number("Type the 2º integer: ")

	# Step 2: Get the sum from a and b.
	result = sum_of_integers(a, b)

	# Step 3: Show the result.
	print(f">>> {a} + {b} = {result}")


def main() -> None:
	# Main: Execute the program using cProfile module.
	cProfile.run('program_profiler()')


if __name__ == "__main__":
	main()
