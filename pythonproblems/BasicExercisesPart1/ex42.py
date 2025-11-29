from platform import architecture


def shell_mode_detector() -> None:
	"""
	This program determines if a Python shell is executing in 32bit or 64bit mode on OS.
	Author: Gustavo Assi Alencar.
	Date:   02/11/2025.
	"""

	# Step 1: Use architecture() method from platform module.
	system_architecture = architecture()
	system_bits = system_architecture[0]
	system_linkage = system_architecture[1]

	# Step 2: Display the information:
	print(f">>> Bits architecture: {system_bits}")
	print(f">>> Linkage architecture: {system_linkage}")


def main() -> None:
	shell_mode_detector()


if __name__ == "__main__":
	main()
