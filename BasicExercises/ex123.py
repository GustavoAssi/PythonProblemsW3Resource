from utils import Input


def get_max(numbers: list) -> int:
    """
    Returns the max value in a list of integers.
    :param numbers: a list of integer numbers.
    :return: the max value.
    """
    largest = numbers[0]
    for number in numbers:
        if number >= largest:
            largest = number
    return largest


def get_min(numbers: list) -> int:
    """
    Returns the min value in a list of integers.
    :param numbers: a list of integer numbers.
    :return: the min value.
    """
    smallest = numbers[0]
    for number in numbers:
        if number <= smallest:
            smallest = number
    return smallest


def max_and_min_of_number_types() -> None:
    """
    This program determines the largest and smallest integers, longs, and floats.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """
    
    # Step 1: Get from user a list of integers.
    numbers = Input.get_list("Type a list of integer numbers: ", elements_type="int")
    
    # Step 2: Display the max and min values.
    largest = get_max(numbers)
    smallest = get_min(numbers)
    print(f">>> Largest = {largest}")
    print(f">>> Smallest = {smallest}")
    
    # Step 3: Assert some tests.
    assert get_max([3, 1, 4, 5, 2]) == 5
    assert get_min([3, 1, 4, 5, 2]) == 1


def main() -> None:
    max_and_min_of_number_types()


if __name__ == "__main__":
    main()
