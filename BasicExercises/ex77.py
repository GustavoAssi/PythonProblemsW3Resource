import sys


def endianess_checker():
	"""
	This program est whether the system is a big-endian platform or a little-endian platform.
	Author: Gustavo Assi Alencar.
	Date:   08/11/2025.
	"""

	# Step 1: Get if system byteorder is little.
	if sys.byteorder == "little":
		print("little-endian platform")
	else:
		print("big-endian platform")


def main():
	endianess_checker()


if __name__ == "__main__":
	main()
