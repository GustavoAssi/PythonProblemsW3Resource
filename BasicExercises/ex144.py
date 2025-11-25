def variable_type_checker() -> None:
    """
    This program checks whether a variable is an integer or string.
    Author: Gustavo Assi Alencar.
    Date:   24/11/2025.
    """

    # Step 1: Set a few variables.
    variable_1 = "Python"
    variable_2 = 42

    # Step 2: Check the variables.
    variables = [variable_1, variable_2]
    for variable in variables:
        if "str" in str(type(variable)):
            print(">>> Is a string")
        elif "int" in str(type(variable)):
            print(">>> Is a integer")


def main():
    variable_type_checker()


if __name__ == "__main__":
    main()
