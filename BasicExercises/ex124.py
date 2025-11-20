from utils import Input


def variable_equality_checker() -> None:
    """
    This program checks whether multiple variables have the same value.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: Get from user 3 variables.
    x = Input.get_string("1º string: ", stripped=True)
    y = Input.get_string("2º string: ", stripped=True)
    z = Input.get_string("3º string: ", stripped=True)

    # Step 2: Check if in fact the variables has the same value.
    if x == y == z:
        print("All equal!")
    else:
        print("Not equal!")


def main() -> None:
    variable_equality_checker()


if __name__ == "__main__":
    main()
