def function_documentation_printer():
	"""
	This program display any function documentation, since the function is Python built-in.
	Author: Gustavo Assi Alencar.
	Date:   27/10/2025.
	"""

	# Step 1: Get the function name from user.
	function_name = input('Type the function name (press "q" to exit): ')

	while function_name.lower() != "q":

		# Step 2: Try to open function documentation using help() function.
		try:
			help(function_name)
		except Exception as e:
			print(f'Failed to open function {function_name} documentation: {e}')

		function_name = input('Type the function name (press "q" to exit): ')


def main():
	function_documentation_printer()


if __name__ == "__main__":
	main()
