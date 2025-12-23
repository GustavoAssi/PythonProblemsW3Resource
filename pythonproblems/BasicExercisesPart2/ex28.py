from pythonproblems.functions.utils import Input


def generate_sequence(first_term, n, r):
    """
    Procedure to generate an arithmetic sequence.
    :param first_term: is the initial value of the sequence.
    :param n: is the number of terms of the sequence.
    :param r: is the value of sequence ratio or displacement.
    """
    term = first_term
    for index in range(n):
        if index != n - 1:
            print(f"{term}, ", end="")
        else:
            print(f"{term}")
        term += r


def series_length_and_terms() -> None:
    """
    This program prints the length of the series and the series
    from the given 3rd term, 3rd last term and the sum of a series.
    Author: Gustavo Assi Alencar.
    Date:   08/12/2025.
    """

    # Step 1: Get values.
    a3 = Input.get_integer_number("Type the value of third element: ")
    an_2 = Input.get_integer_number("Type the value of third last element: ")
    sum_of_series = Input.get_integer_number("Type the sum of the series: ")

    # Step 2: Get number of elements.
    n = int(2 * sum_of_series / (a3 + an_2))
    print(f">>> Length of the series: {n}")

    # Step 3: Generate a sequence.
    if n == 5:
        print("When the number of the terms is equal to five, ", end="")
        print("any value for ratio will satisfy the problem.")
        for r in range(0, 10):
            first_term = a3 - 2*r
            generate_sequence(first_term, n, r)
    else:
        r = (an_2 - a3) / (n - 5)
        first_term = a3 - 2*r
        generate_sequence(first_term, n, r)


def main() -> None:
    series_length_and_terms()


if __name__ == "__main__":
    main()
