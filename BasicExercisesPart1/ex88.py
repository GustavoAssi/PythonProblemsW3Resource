from utils import Input


def sum_expression_printer() -> None:
    """
    This program calculates x + y given variables x and y.
    Author: Gustavo Assi Alencar.
    Date:   13/11/2025.
    """

    # Step 1: Get x and y from user.
    x = Input.get_float_number("Type the value of x: ")
    y = Input.get_float_number("Type the value of y: ")

    # Step 2: Display x + y result.
    print(f">>> {x} + {y} = {x + y}")


def main() -> None:
    sum_expression_printer()


if __name__ == "__main__":
    main()
