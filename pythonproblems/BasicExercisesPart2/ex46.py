import datetime
from pythonproblems.functions.utils import Input


def day_of_date_finder() -> None:
    """
    This program reads a date (from 2016/1/1 to 2016/12/31) and prints the day of the date.
    Author: Gustavo Assi Alencar.
    Date:   25/12/2025.
    """

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Step 1: Get a date from user.
    year = Input.get_integer_number("Input the year: ", must_be_positive=True)
    month = Input.get_integer_number("Input the month: ", must_be_positive=True)
    day = Input.get_integer_number("Input the day: ", must_be_positive=True)

    # Step 2: With datetime module, get the day of week.
    try:
        date = datetime.date(year=year, month=month, day=day)
        weekday = weekdays[date.weekday()]

        # Step 3: Display the result.
        print(f"The weekday on this date {year}/{month}/{day} is {weekday}")

    except Exception as e:
        print(f"Invalid date: {e}")


def main() -> None:
    day_of_date_finder()


if __name__ == "__main__":
    main()
