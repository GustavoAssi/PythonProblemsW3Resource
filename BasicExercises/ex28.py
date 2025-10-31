from utils import Input


def even_numbers_until_237():
	"""
	This program print all even numbers until 237 from a given list of numbers.
	Author: Gustavo Assi Alencar.
	Date:   31/10/2025.
	"""

	# Step 1: Set the given list
	numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

	# Step 2: Get all even numbers until 237.
	for number in numbers:
		if number % 2 == 0:
			print(number)
		elif number == 237:
			print(number)
			break

def main():
	even_numbers_until_237()


if __name__ == "__main__":
	main()