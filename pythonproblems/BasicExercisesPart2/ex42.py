from pythonproblems.functions.utils import Input


def sort_six_numbers() -> None:
    """
    This program accepts six numbers as input and sorts them in descending order.
    Author: Gustavo Assi Alencar.
    Date:   25/12/2025.
    """

    # Step 1: Get the numbers.
    numbers = Input.get_list("Type a few numbers (comma separated): ", elements_type="int")

    # Step 2: Sort the numbers in reverse order.
    sorted_numbers = sorted(numbers, reverse=True)

    # Step 3: Display numbers in reverse order.
    print(f">>> sorted numbers in reverse order: ", end="")

    amount_of_numbers = len(sorted_numbers)
    for index in range(amount_of_numbers):
        if index != amount_of_numbers -1:
            print(f"{sorted_numbers[index]}, ", end="")
        else:
            print(f"{sorted_numbers[index]}\n")


def main() -> None:
    sort_six_numbers()


if __name__ == "__main__":
    main()
