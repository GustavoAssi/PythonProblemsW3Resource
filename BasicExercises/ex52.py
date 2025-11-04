from __future__ import print_function
import sys


def eprint(*args, **kwargs):
	"""
	Call the print function to print the standard error stream.
	"""

	# Using 'file=sys.stderr' to print the standard error stream.
	print(*args, file=sys.stderr, **kwargs)


def print_to_STDERR():
	"""
	This program print to STDERR.
	Author: Gustavo Assi Alencar.
	Date:   04/11/2025.
	"""

	# Step 1: Run eprint function with "abc", "efg", "xyz" as argmunts and "--" as separator.
	eprint("abc", "efg", "xyz", sep="--")


def main():
	print_to_STDERR()


if __name__ == "__main__":
	main()
