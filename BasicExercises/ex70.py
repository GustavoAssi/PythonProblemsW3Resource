import glob
import os


def sort_files_by_date():
	"""
	This program sort files by date.
	Author: Gustavo Assi Alencar.
	Date:   05/11/2025.
	"""

	# Step 1: Just sort using glob and os modules.
	files = glob.glob("*.py")
	files.sort(key=os.path.getmtime)

	# Step 2: Display files list.
	print("\n".join(files))


def main():
	sort_files_by_date()


if __name__ == "__main__":
	main()
