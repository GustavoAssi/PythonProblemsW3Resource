import os
import time


def directory_listing_by_creation_date() -> None:
	"""
	This program gets a directory listing, sorted by creation date.
	Author: Gustavo Assi Alencar.
	Date:   06/11/2025.
	"""

	# Step 2: Sort directory by creation date.
	paths = ["%s %s" % (time.ctime(t), f) for t, f in sorted([(os.path.getctime(x), x) for x in os.listdir("")])]

	# Step 3: Display results.
	print("Directory listing, sorted by creation time: ")
	for file in paths:
		print(file)


def main() -> None:
	directory_listing_by_creation_date()


if __name__ == "__main__":
	main()
