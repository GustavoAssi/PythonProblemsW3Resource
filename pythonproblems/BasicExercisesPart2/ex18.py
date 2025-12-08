from pythonproblems.functions.utils import Input


def find_median_of_three() -> None:
    """
    This program finds the median among three given numbers.
    Author: Gustavo Assi Alencar.
    Date:   29/11/2025.
    """

    # Step 1: Get three values.
    number_1 = Input.get_float_number("Type the 1º number: ")
    number_2 = Input.get_float_number("Type the 2º number: ")
    number_3 = Input.get_float_number("Type the 3º number: ")

    # Step 2: Find the median.
    numbers = sorted([number_1, number_2, number_3])
    median = numbers[1]
    print(f">>> Median: {median}")


def main() -> None:
    find_median_of_three()


if __name__ == "__main__":
    main()
