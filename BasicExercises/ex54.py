import os
import pwd


def get_username():
	"""
	Returns username using pwd and os modules.
	"""
	return pwd.getpwuid(os.geteuid())[0]


def get_current_username():
	"""
	This program get the current username.
	Author: Gustavo Assi Alencar.
	Date:   04/11/2025.
	"""

	# Step 1: Get username by custom function 'get_username':
	user = get_username()

	# Step 2: Display the information.
	print(f">>> user: {user}")


def main():
	get_current_username()


if __name__ == "__main__":
	main()
