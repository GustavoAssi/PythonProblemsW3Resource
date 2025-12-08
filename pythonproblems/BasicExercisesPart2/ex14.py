from pythonproblems.functions.utils import Input


def add_without_plus() -> None:
    """
    This program adds two positive integers without using the '+' operator.
    Author: Gustavo Assi Alencar.
    Date:   29/11/2025.
    """

    # Step 1: Get two integer numbers from user.
    a = Input.get_integer_number("1º integer: ", must_be_positive=True)
    b = Input.get_integer_number("2º integer: ", must_be_positive=True)

    # Step 2: Add the numbers using binary operations.
    while b != 0:
        data = a & b  # Bitwise operation between a and b stored on carry variable.
        a = a ^ b     # XOR between a and b.
        b = data << 1 # Left shift on carry by 1 position

    # Step 3: After loop, "a" will store the resul of sum.
    print(f">>> {a}")


def main() -> None:
    add_without_plus()


if __name__ == "__main__":
    main()
