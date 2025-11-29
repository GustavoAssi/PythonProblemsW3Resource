from pythonproblems.functions.utils import Input


def has_unique_elemens(numbers: list) -> bool:
    """
    Returns True if a list of elements has unique elements.
    :param numbers: (list) List of numbers.
    :return:        (bool) True or False.
    """
    n = len(numbers)
    for i_index in range(0, n):
        for j_index in range(i_index + 1, n):
            if numbers[i_index] == numbers[j_index]:
                return False
    return True


def unique_numbers_check() -> None:
    """
    This program takes a sequence of numbers and determines
    whether all the numbers are different from each other.
    Author: Gustavo Assi Alencar.
    Date:   26/11/2025.
    """

    # Step 1: Get the numbers sequence.
    numbers = Input.get_list("Type a list of integer numbers: ", elements_type="int")

    # Step 2: Check if the numbers are unique.
    if has_unique_elemens(numbers):
        print(">>> Has unique elements.")
    else:
        print(">>> Not unique elements. ")


def main() -> None:
    unique_numbers_check()


if __name__ == "__main__":
    main()
