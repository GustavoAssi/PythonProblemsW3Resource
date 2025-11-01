from utils import Input
from math import sqrt


def distance_between_points():
	"""
	This program compute the distance between the points (x1, y1) and (x2, y2).
	Author: Gustavo Assi Alencar.
	Date:   01/11/2025.
	"""

	# Step 1: Get the coordinates from user.
	x1 = Input.get_float_number("Type value of x1: ")
	y1 = Input.get_float_number("Type value of y1: ")
	x2 = Input.get_float_number("Type value of x2: ")
	y2 = Input.get_float_number("Type value of y2: ")
	
	# Step 2: Compute the distance.
	distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
	
	# Step 3: Display result.
	print(f">>> distance: {distance}")

def main():
	distance_between_points()


if __name__ == "__main__":
	main()
