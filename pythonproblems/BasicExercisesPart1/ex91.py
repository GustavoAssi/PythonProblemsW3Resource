from pythonproblems.functions.utils import Input


def swap_variables() -> None:
    """
    This program swap two variables.
    Author: Gustavo Assi Alencar.
    Date:   13/11/2025.
    """

    # Step 1: Get two variables.
    x = Input.get_integer_number("Type x value: ")
    y = Input.get_integer_number("Type y value: ")
    print(f">>> x = {x}, y = {y}")

    # Step 2: Swap them.
    x, y = y, x

    # Step 3: Display the result.
    print("\n")
    print(f">>> Swaped variables")
    print(f">>> x = {x}, y = {y}")


def main() -> None:
    swap_variables()


if __name__ == "__main__":
    main()
