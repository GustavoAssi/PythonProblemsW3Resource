import multiprocessing


def cpu_count_finder():
	"""
	This program find out the number of CPUs used.
	Author: Gustavo Assi Alencar.
	Date:   03/11/2025.
	"""

	# Step 1: Get the cpu count by multiprocessing module.
	cpu_count = multiprocessing.cpu_count()

	# Step 2: Display information.
	print(f">>> CPU count: {cpu_count}")


def main():
	cpu_count_finder()


if __name__ == "__main__":
	main()
