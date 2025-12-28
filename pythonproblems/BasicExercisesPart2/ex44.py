from pythonproblems.functions.utils import Input


def max_subsequence_sum() -> None:
    """
    This program finds the maximum sum of a contiguous subsequence 
    from a given sequence of numbers a1, a2, a3, ... an.
    Author: Gustavo Assi Alencar.
    Date:   25/12/2025.
    """

    # Step 1: Get the max number of values.
    n = Input.get_integer_number("Type the max number of values: ", must_be_positive=True)

    # Step 2: Start get numbers and compute the sum.
    counter = 0
    s_value = 0
    while counter < n:
        number = Input.get_float_number("Type a number (type 0 to finish): ")
        counter += 1
        s_value += number
        if number == 0:
            break

    # Step 3: Display results.
    print(f">>> Sum: {s_value}")


def main() -> None:
    max_subsequence_sum()


if __name__ == "__main__":
    main()
