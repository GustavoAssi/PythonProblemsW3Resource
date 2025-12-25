from pythonproblems.functions.utils import Input


def debt_calculation() -> None:
    """
    This program computes the amount of debt in n months.
    Each month, the loan adds 5% interest to the $100,000 debt and rounds to the nearest 1,000 above.
    Author: Gustavo Assi Alencar.
    Date:   23/12/2025.
    """

    # Step 1: Get some data.
    initial_amount = Input.get_float_number("Type the initial amount ($): ", must_be_positive=True)
    tax_value = Input.get_integer_number("Type the value of the tax per month (%): ", must_be_positive=True)
    time_in_months = Input.get_integer_number("Type the time in months: ", must_be_positive=True)

    # Step 2: Compute the amount of debt.
    amount_of_debt = round(initial_amount * (1 + (tax_value / 100))**time_in_months, 3)
    print(f">>> Amount of debt: {amount_of_debt}")


def main() -> None:
    debt_calculation()


if __name__ == "__main__":
    main()
