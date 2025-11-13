from utils import Input


def sum_of_first_positives() -> None:
	"""
	This program sums the first n positive integers.
	Author: Gustavo Assi Alencar.
	Date:   04/11/2025.
	"""
	
	# Step 1: Get value of n.
	n = Input.get_integer_number("Type a value of a positive integer: ", must_be_positive=True)

	# Step 2: Compute the sum of first n positive integers.
	s = 0
	for term in range(1, n + 1):
		s += term

	# Step 3: Display the results.
	print(f">>> Sum of first {n} positive integers: {s}")
	

def main() -> None:
	sum_of_first_positives()


if __name__ == "__main__":
	main()

