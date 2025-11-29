from time import sleep
from pythonproblems.functions.utils import Input


def remove_every_third() -> None:
    """
    This program removes and prints every third number
    from a list of numbers until the list is empty.
    Author: Gustavo Assi Alencar.
    Date:   26/11/2025.
    """

    # Step 1: Get a list from user.
    numbers = Input.get_list("Type a list of numbers: ", elements_type="int")

    # Step 2: Start removing the third number from the list.
    while len(numbers) > 0:
        middle = len(numbers) // 2
        removed_element = numbers.pop(middle)
        print(f">>> Removed element: {removed_element}")
        print(f">>> Current list: {numbers}\n")
        sleep(1)

def main() -> None:
    remove_every_third()


if __name__ == "__main__":
    main()
