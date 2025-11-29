def variable_defined_checker() -> None:
    """
    This program determines if a variable is defined or not.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: For some variables use try/except statement to handle NameError Exception.
    try:
        x = 1
        print(f">>> x = {x}")
    except NameError:
        print("Variable is not defined")
    else:
        print("Variable is defined")

    try:
        print(f">>> y = {y}")
    except NameError:
        print("Variable is not defined")
    else:
        print("Variable is defined")


def main() -> None:
    variable_defined_checker()


if __name__ == "__main__":
    main()
