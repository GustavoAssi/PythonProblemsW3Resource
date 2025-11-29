from pythonproblems.functions.utils import Input


def first_and_last_colors() -> None:
	"""
	This program displays the first and the last color from a list of colors.
	Author: Gustavo Assi Alencar.
	Date:   26/10/2025.
	"""
	
	# Step 1: Get colors from user.
	colors = Input.get_string("Input the colors list: ")
	colors_list = [
		color.strip() for color in colors.split(",")
	]
	
	# Step 2: Get first and last, then display output.
	first, last = colors_list[0], colors_list[-1]
	print(f">>> First color: {first}")
	print(f">>> Last color: {last}")


def main() -> None:
	first_and_last_colors()


if __name__ == "__main__":
	main()
