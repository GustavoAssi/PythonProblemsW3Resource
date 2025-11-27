from inspect import getmodule


def some_function() -> None:
    pass


def get_module_object() -> None:
    """
    This program gets the actual module object for a given object.
    Author: Gustavo Assi Alencar.
    Date:   20/11/2025.
    """

    # Step 1: Set any Python object.
    string = "Python"

    # Step 2: Use getmodule function from inspect module.
    print(">>> From a string in this script: ", getmodule(string))
    print(">>> From a function in this script: ", getmodule(some_function))


def main():
    get_module_object()


if __name__ == "__main__":
    main()
