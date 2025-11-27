def split_variable_length_string() -> None:
    """
    This program splits a variable length string into variables.
    Author: Gustavo Assi Alencar.
    Date:   20/11/2025.
    """

    # Step 1: Set a list of values.
    values = ['a', 'b', 'c']

    # Step 2: Assign values for variables.
    # OBS: This works since the number of variables is the same of the length of elements in the list.
    x, y, z = values

    # Step 3: Display results.
    print(f">>> x = {x}")
    print(f">>> y = {y}")
    print(f">>> z = {z}")


def main():
    split_variable_length_string()


if __name__ == "__main__":
    main()
