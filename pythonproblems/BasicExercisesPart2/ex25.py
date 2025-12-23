from pythonproblems.functions.utils import Input


def missing_digits_finder() -> None:
    """
    This program finds the digits that are missing from a given mobile number.
    Author: Gustavo Assi Alencar.
    Date:   08/12/2025.
    """

    # Step 1: Get a mobile number from user.
    mobile_number = Input.get_string("Type the mobile number: ", stripped=True)
    mobile_number = mobile_number.replace('-', '').replace(' ', '')
    mobile_number = mobile_number.replace('(', '').replace(')', '')

    # Step 2: Display the absent numbers.
    mobile_numbers = set(list(mobile_number))
    all_numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    absent_numbers = sorted(mobile_numbers.symmetric_difference(all_numbers))
    print(f">>> Absent numbers: {absent_numbers}")


def main() -> None:
    missing_digits_finder()


if __name__ == "__main__":
    main()
