import calendar


months = {
	"january": 1, 
	"february": 2, 
	"march": 3, 
	"april": 4,
	"may": 5, 
	"june": 6, 
	"july": 7, 
	"august": 8, 
	"september": 9, 
	"october": 10, 
	"november": 11, 
	"december": 12
}


def display_calendar():
	"""
	This program is able to show a calendar from a given year and month.
	Author: Gustavo Assi Alencar.
	Date:   27/10/2025.
	"""
	
	# Step 1: Get the year from user.
	year = int(input("Type the year: "))

	# Step 2: Get the month from user and display month days.
	month_name = input("Type the month (january, february, ...): ")
	try:
		month = months[month_name.lower().strip()]
		text_calendar = calendar.TextCalendar()
		print(text_calendar.formatmonth(theyear=year, themonth=month))
	except KeyError:
		print(f'Failed to display month days: "{month_name}" is a invalid input!')
	

def main():
	display_calendar()


if __name__ == "__main__":
	main()
