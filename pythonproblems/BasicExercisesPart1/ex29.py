from pythonproblems.functions.utils import Input


def unique_colors_finder() -> None:
	"""
	This program prints out all colors from color_list_1 that are not present in color_list_2.
	Author: Gustavo Assi Alencar.
	Date:   31/10/2025.
	"""
	
	# Step 1: Get colors lists.
	colors_1 = Input.get_string("Type 1º group of colors: ")
	colors_list_1 = [color.strip() for color in colors_1.split(",")]
	colors_2 = Input.get_string("Type 2º group of colors: ")
	colors_list_2 = [color.strip() for color in colors_2.split(",")]

	# Step 2: Get all colors from list 1 that are not present in list 2.
	diff = list(set(colors_list_1) - set(colors_list_2))

	# Step 3: Display the result.
	print(f">>> {diff}")


def main() -> None:
	unique_colors_finder()


if __name__ == "__main__":
	main()