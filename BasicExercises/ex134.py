def input_two_integers() -> None:
    """
    This program inputs two integers on a single line.
    Author: Gustavo Assi Alencar.
    Date:   20/11/2025.
    """

    # Step 1: Reproduce the two integer input in single line.
    try:
        x, y = [int(value) for value in input("Type two integers separated by space: ").split()]

        # Step 2: Just the print the numbers.
        print(f">>> x = {x}")
        print(f">>> x = {y}")

    except ValueError as e:
        print(f"Too many values, type only two values -> {e}")


def main():
    input_two_integers()


if __name__ == "__main__":
    main()
