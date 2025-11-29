from pythonproblems.functions.utils import Input


def filter_positive_numbers() -> None:
    """
    This program filters positive numbers from a list.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: Get from user a list.
    numbers = Input.get_list("Input a list of integer numbers: ", elements_type="int")
    print(f">>> Original list: {numbers}")

    # Step 2: Remove first item.
    positives = list(filter(lambda x: x > 0, numbers))

    # Step 3: Display results.
    print(f">>> Positive itens: {positives}")


def main() -> None:
    filter_positive_numbers()


if __name__ == "__main__":
    main()
