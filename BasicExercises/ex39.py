from utils import Input


def future_value_calculator():
	"""
	This program compute the future value of a specified principal amount, rate of interest, and number of years.
	Author: Gustavo Assi Alencar.
	Date:   01/11/2025.
	"""

	# Step 1: Get the amount, rate of interest and number of years from user.
	amount = Input.get_float_number("Amount: R$ ") 
	rate_of_interest = Input.get_float_number("Rate of interest per year: ")
	number_of_years = Input.get_integer_number("Years: ", must_be_positive=True)

	# Step 2: Compute the future value.
	future_value_simple_interest = amount * (1 + rate_of_interest * number_of_years)
	future_value_compound_interest = amount * pow((1 + rate_of_interest), number_of_years)

	# Step 3: Display the result.
	print(f">>> Future Value Simple Interest: R$ {future_value_simple_interest:.3f}")
	print(f">>> Future Compound Simple Interest: R$ {future_value_compound_interest:.3f}")


def main():
	future_value_calculator()


if __name__ == "__main__":
	main()
