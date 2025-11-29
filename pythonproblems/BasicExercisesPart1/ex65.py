from pythonproblems.functions.utils import Input


def seconds_to_DHMS_converter() -> None:
	"""
	This program converts seconds into days, hours, minutes, and seconds.
	Author: Gustavo Assi Alencar.
	Date:   04/11/2025.
	"""

	# Step 1: Get total amount of seconds.
	total_seconds = Input.get_integer_number("Total amount of seconds: ", must_be_positive=True)

	# Step 2: Separate total time into days, hours, minutes and seconds.
	days = total_seconds // 86400
	hours = total_seconds % 86400 // 3600
	minutes = total_seconds % 86400 % 3600 // 60
	seconds = total_seconds % 86400 % 3600 % 60

	# Step 3: Display results.
	print(f">>> {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")


def main() -> None:
	seconds_to_DHMS_converter()


if __name__ == "__main__":
	main()
