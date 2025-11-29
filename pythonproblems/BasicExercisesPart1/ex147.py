from pythonproblems.functions.utils import Input


def divisibility_tester() -> None:
    """
    This program checks whether a number is divisible by another number.
    Author: Gustavo Assi Alencar.
    Date:   25/11/2025.
    """

    # Step 1: Get two integer numbers from user.
    a = Input.get_integer_number("Type the 1º integer: ")
    b = Input.get_integer_number("Type the 2º integer: ", must_be_positive=True)

    # Step 2: Test divisibility.
    if a % b == 0:
        print(f">>> {b} divides {a}")
    else:
        print(f">>> {b} can't divide {a}")


def main():
    divisibility_tester()


if __name__ == "__main__":
    main()
