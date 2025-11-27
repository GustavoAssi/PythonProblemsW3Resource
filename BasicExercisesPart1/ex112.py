from utils import Input


def remove_first_list_item() -> None:
    """
    This program removes the first item from a specified list.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: Get from user a list.
    input_list = Input.get_list("Input a list of integer numbers: ", elements_type="int")
    print(f">>> Original list: {input_list}")

    # Step 2: Remove first item.
    input_list.remove(input_list[0])

    # Step 3: Display results.
    print(f">>> List without first item: {input_list}")


def main() -> None:
    remove_first_list_item()


if __name__ == "__main__":
    main()
