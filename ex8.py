def first_and_last_colors():
	"""
	This program display the first and the last color from a list of colors.
	Author: Gustavo Assi Alencar.
	Date:   26/10/2025.
	"""
	
	# Step 1: Get colors from user.
	colors_list = [
		color.strip() for color in input("Input the colors list: ").split(",")
	]
	
	# Step 2: Get first and last, then display output.
	first, last = colors_list[0], colors_list[-1]
	print(f">>> First color: {first}")
	print(f">>> Last color: {last}")


def main():
	first_and_last_colors()


if __name__ == "__main__":
	main()
