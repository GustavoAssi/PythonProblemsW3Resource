def list_special_variables() -> None:
    """
    This program lists the special variables used in the language.
    Author: Gustavo Assi Alencar.
    Date:   13/11/2025.
    """

    # Step 1: Create a set 's_var_names' containing unique variable names in the global namespace.
    s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))

    # Step 2: Print an empty line for formatting.
    print()

    # Step 3: Join variable names in groups of 8 and print them for better readability.
    for name in s_var_names:
        print(name)

    # Step 4: Print an empty line for formatting.
    print()


def main() -> None:
    list_special_variables()


if __name__ == "__main__":
    main()
