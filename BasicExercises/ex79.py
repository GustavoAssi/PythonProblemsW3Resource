from sys import getsizeof


def object_size_finder() -> None:
	"""
	This program gets the size of an object in bytes.
	Author: Gustavo Assi Alencar.
	Date:   08/11/2025.
	"""

	# Step 1: Set some python objects.
	integer_number = 2025
	float_number = 3.1415
	string = "Gustavo Assi Alencar"
	list_of_subjects = ["Python", "Algorithms", "Data Structures", "Mathematics"]

	# Step 2: From each object, display the size in bytes.
	objects = (integer_number, float_number, string, list_of_subjects)
	for object in objects:
		print(f">>> {object}: {getsizeof(object)} bytes")


def main() -> None:
	object_size_finder()


if __name__ == "__main__":
	main()
