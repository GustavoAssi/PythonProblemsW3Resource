import os


def access_enviroment_variables() -> None:
	"""
	This program access environment variables.
	Author: Gustavo Assi Alencar.
	Date:   04/11/2025.
	"""

	# Step 1: Output some enviroment variables.
	print("-" * 50)
	print(f">>> HOME: {os.environ['HOME']}")
	print("-" * 50)
	print(f">>> PATH: {os.environ['PATH']}")
	print("-" * 50)
	print('\n')

	# Step 2: Print all the enviroment variables.
	for variable, value in os.environ.items():
		print(f">>> {variable}: {value}")
		print("-" * 50)


def main() -> None:
	access_enviroment_variables()


if __name__ == "__main__":
	main()
