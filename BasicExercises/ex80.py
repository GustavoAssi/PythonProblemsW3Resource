import sys


def current_recursion_limit():
	"""
	This program current value of the recursion limit.
	Author: Gustavo Assi Alencar.
	Date:   08/11/2025.
	"""

	# Step 1: Display recursion limit using sys module.
	print(f">>> Recursion limit value: {sys.getrecursionlimit()}")


def main():
	current_recursion_limit()


if __name__ == "__main__":
	main()
