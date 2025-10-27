import datetime


def days_between_dates():
	"""
	This program calculate the difference between two days.
	Author: Gustavo Assi Alencar.
	Date: 27/10/2025.
	"""

	# Step 1: Get dates from user.
	date_1 = input("Type 1º date: ").lower().strip().split("/")
	date_2 = input("Type 2º date: ").lower().strip().split("/")
	date_1_values = {"day": int(date_1[0]), "month": int(date_1[1]), "year": int(date_1[2])}
	date_2_values = {"day": int(date_2[0]), "month": int(date_2[1]), "year": int(date_2[2])}

	# Step 2: Get dates difference using datetime.date function.
	datetime_1 = datetime.date(date_1_values["year"], date_1_values["month"], date_1_values["day"])
	datetime_2 = datetime.date(date_2_values["year"], date_2_values["month"], date_2_values["day"])
	time_difference = datetime_2 - datetime_1

	# Step 3: Show output 
	print(abs(time_difference))


def main():
	days_between_dates()


if __name__ == "__main__":
	main()