import importlib.util


def locate_python_module_sources() -> None:
    """
    This program finds the location of Python module sources.
    Author: Gustavo Assi Alencar.
    Date:   25/11/2025.
    """

    # Step 1: Set some built-in modules.
    modules = ['os', 'sys', 'math', 'time']

    # Step 2: Find modules locations using importlib module.
    for module in modules:
        spec = importlib.util.find_spec(module)
        print(f">>> {spec}")


def main():
    locate_python_module_sources()


if __name__ == "__main__":
    main()
