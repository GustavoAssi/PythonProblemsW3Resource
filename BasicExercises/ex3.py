import datetime



def current_date_time_display() -> None:
	"""
	This program displays current date and time.
	Author: Gustavo Assi Alencar.
	Date:   26/10/2025.
	"""
	
	current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	print(f"{current_datetime}")
	

def main() -> None:
	current_date_time_display()


if __name__ == "__main__":
	main()