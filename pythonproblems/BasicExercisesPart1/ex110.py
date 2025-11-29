from pythonproblems.functions.utils import Input


def divisible_by_fifteen_finder() -> None:
    """
    This program gets numbers divisible by fifteen from a list using an anonymous function.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: Get the numbers.
    numbers = Input.get_string("Type integer the numbers: ", stripped=True)
    numbers_list = [int(value.strip()) for value in numbers.split(",")]

    # Step 2: Apply filter using anonymous function (lambda function).
    divisible_by_fifteen = list(filter(lambda x: (x % 15 == 0), numbers_list))

    # Step 3: Display the result.
    print(f">>> Numbers divisible by 15: {divisible_by_fifteen}")


def main() -> None:
    divisible_by_fifteen_finder()


if __name__ == "__main__":
    main()
