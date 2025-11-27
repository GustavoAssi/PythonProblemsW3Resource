from utils import Input


def add_integers_validator() -> None:
	"""
	This program adds two objects if both objects are integers.
	Author: Gustavo Assi Alencar.
	Date:   01/11/2025.
	"""

	# Step 1: Get the objects from user.
	obj_1 = Input.get_integer_number("Type an object: ")
	obj_2 = Input.get_integer_number("Type an object: ")

	# Step 2: Add the objects if both are integers.
	if isinstance(obj_1, int) and isinstance(obj_2, int):
		print(f">>> {obj_1} + {obj_2} = {obj_1 + obj_2}")


def main() -> None:
	add_integers_validator()


if __name__ == "__main__":
	main()
