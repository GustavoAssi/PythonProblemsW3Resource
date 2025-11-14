import traceback


def f1():
    traceback.print_stack()


def f2():
    return f1()


def print_call_stack() -> None:
    """
    This program prints the current call stack.
    Author: Gustavo Assi Alencar.
    Date:   13/11/2025.
    """

    # Step 1: Call f2() to call f1() to call traceback.print_stack()
    f2()


def main() -> None:
    print_call_stack()


if __name__ == "__main__":
    main()
