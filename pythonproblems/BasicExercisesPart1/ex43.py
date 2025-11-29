import platform


def os_and_platform_info() -> None:
	"""
	This program gets the OS name, platform and release information from user's machine.
	Author: Gustavo Assi Alencar.
	Date:   02/11/2025.
	"""

	# Step 1: Get OS name, platform and release information by platform module.
	os_name = platform.system()
	platform_name = platform.platform()
	release = platform.release()

	# Step 2: Display the information.
	print(f">>> OS name: {os_name}")
	print(f">>> Platform: {platform_name}")
	print(f">>> Release: {release}")


def main() -> None:
	os_and_platform_info()


if __name__ == "__main__":
	main()
