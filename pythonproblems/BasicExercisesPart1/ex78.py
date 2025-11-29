import sys


def list_built_in_modules() -> None:
	"""
	This program finds the available built-in modules.
	Author: Gustavo Assi Alencar.
	Date:   08/11/2025.
	"""

	# Step 1: Get all built-in modules using sys.builtin_modules_names.
	builtin_modules = sys.builtin_module_names

	# Step 2: Display all of them.
	for module in builtin_modules:
		print(f">>> {module}")


def main() -> None:
	list_built_in_modules()


if __name__ == "__main__":
	main()
