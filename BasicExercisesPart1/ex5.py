from utils import Input


def reverse_full_name() -> None:
	"""
	This program gets the first and last name from user and display it in reverse order.
	Author: Gustavo Assi Alencar.
	Date:   26/10/2025.
	"""

	# Step 1: Get user's full name separeted.
	full_name = Input.get_string("Type your first and last name: ", stripped=True)
	full_name_list = full_name.split()

	# Step 2: Show the name in reverse order.
	if len(full_name_list) == 2:
		first_name, last_name = full_name_list[0], full_name_list[1]
		reverse_name = last_name + " " + first_name
		print(f">>> {reverse_name}")
	else:
		print("User should input just first and last name!")


def main() -> None:
	reverse_full_name()


if __name__ == "__main__":
	main()