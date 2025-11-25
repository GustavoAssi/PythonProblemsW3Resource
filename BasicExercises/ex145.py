def check_list_tuple_or_set() -> None:
    """
    This program tests if a variable is a list, tuple, or set.
    Author: Gustavo Assi Alencar.
    Date:   24/11/2025.
    """

    # Step 1: Set a few variables.
    variable_1 = (1, 2, 3)
    variable_2 = [1, 2, 3]
    variable_3 = {1, 2, 3}

    # Step 2: Check the variables.
    variables = [variable_1, variable_2, variable_3]
    for variable in variables:
        if "tuple" in str(type(variable)):
            print(">>> Is a tuple")
        elif "list" in str(type(variable)):
            print(">>> Is a list")
        elif "set" in str(type(variable)):
            print(">>> Is a set")

def main():
    check_list_tuple_or_set()


if __name__ == "__main__":
    main()
