from utils import Input


def time_to_seconds_converter():
	"""
	This program convert all units of time into seconds.
	Author: Gustavo Assi Alencar.
	Date:   04/11/2025.
	"""

	# Step 1: Get days, hours, minutes and seconds from user.
	days = Input.get_integer_number("Input days: ", must_be_positive=True)
	hours = Input.get_integer_number("Input hours: ", must_be_positive=True)
	minutes = Input.get_integer_number("Input minutes: ", must_be_positive=True)
	seconds = Input.get_integer_number("Input seconds: ", must_be_positive=True)

	# Step 2: Convert total time in seconds.
	total_seconds = seconds + 60 * minutes + 3600 * hours + 86400 * days

	# Step 3: Display results.
	print(f">>> Total amount of seconds: {total_seconds}")


def main():
	time_to_seconds_converter()


if __name__ == "__main__":
	main()
