from pythonproblems.functions.utils import Input


def sequential_powers_of_two() -> None:
    """
    This program finds the value of n when n degrees of number 2
    are written sequentially on a line without spaces between them.
    Author: Gustavo Assi Alencar.
    Date:   29/11/2025.
    """

    # Step 1: Get the sequence from user.
    sequence = Input.get_string("Type the sequence of degrees of number 2: ")

    # Step 2: Start the search of many degrees of number 2 in the sequence.
    base, i = 2, 1
    while True:
        if str(base ** i) in sequence:
            i += 1
        else:
            break

    print(f">>> Number of degrees in sequence: {i - 1}")


def main() -> None:
    sequential_powers_of_two()


if __name__ == "__main__":
    main()
