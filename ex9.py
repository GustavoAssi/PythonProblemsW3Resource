def exam_schedule_formatter():
	"""
	This program extracts the date from a variable exam_st_date.
	Author: Gustavo Assi Alencar.
	Date:   27/10/2025.
	"""
	
	# Step 1: Set a date variable.
	exam_st_date = (27, 10, 2025)

	# Step 2: Get day (d), month (m), year (y).
	d = exam_st_date[0]
	m = exam_st_date[1]
	y = exam_st_date[2]

	# Step 3: Output the date.
	print(f"The examination date will start from: {d}/{m}/{y}")


def main():
	exam_schedule_formatter()


if __name__ == "__main__":
	main()