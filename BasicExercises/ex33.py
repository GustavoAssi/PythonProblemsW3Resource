from utils import Input


def has_three_equal_values(n1: int, n2: int, n3: int) -> bool:
	"""
	Given 3 integers, returns True if any pair of them are equal.

	:param n1: (int) 1º integer.
	:param n2: (int) 2º integer.
	:param n3: (int) 3º integer.
	:return:   (bool) True or False
	"""
	
	return n1 == n2 or n2 == n3 or n1 == n3


def triple_sum_with_equality():
	"""
	This program sum three given integers. However. 
	If two values are equal, the sum will be zero.
	Author: Gustavo Assi Alencar.
	Date:   31/10/2025.
	"""
	
	# Step 1: Get three integers from user.
	i1 = Input.get_integer_number("Type the 1º integer: ")
	i2 = Input.get_integer_number("Type the 2º integer: ")
	i3 = Input.get_integer_number("Type the 3º integer: ")

	# Step 2: Validate condition.
	if has_three_equal_values(i1, i2, i3):
		sum = 0
	else:
		sum = i1 + i2 + i3

	# Step 3: Display the result
	print(f">>> {sum}")


def main():
	triple_sum_with_equality()


if __name__ == "__main__":
	main()
