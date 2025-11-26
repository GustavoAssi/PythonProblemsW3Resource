from utils import Input


def max_and_min_without_builtins() -> None:
    """
    This program finds the maximum and minimum numbers from a sequence of numbers.
    Author: Gustavo Assi Alencar.
    Date:   25/11/2025.
    """

    # Step 1: Get a list of elements.
    numbers = Input.get_list("Insert a few integers: ", elements_type="int")

    # Step 2: Get the maximum and minimum values.
    maximum = minimum = numbers[0]
    for number in numbers:
        if number >= maximum:
            maximum = number
        if number <= minimum:
            minimum = number

    # Step 3: Display values.
    print(f">>> maximum: {maximum}")
    print(f">>> minimum: {minimum}")


def main():
    max_and_min_without_builtins()


if __name__ == "__main__":
    main()
