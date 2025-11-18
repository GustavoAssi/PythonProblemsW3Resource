from utils import Input


def get_elements_product(numbers: list) -> int:
    """
    Returns the product from a list of integers.
    :param numbers: (list) the list of integer numbers.
    :return:        (int)  the product of the elements from the list
    """
    if len(numbers) > 0:
        return numbers.pop(0) * get_elements_product(numbers)
    return 1


def list_product_calculator() -> None:
    """
    This program computes the product of a list of integers (without using a for loop).
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: Get from user a list.
    numbers = Input.get_list("Input a list of integer numbers: ", elements_type="int")
    print(f">>> Original list: {numbers}")

    # Step 2: Remove first item.
    product = get_elements_product(numbers)

    # Step 3: Display product.
    print(f">>> Product of itens: {product}")


def main() -> None:
    list_product_calculator()


if __name__ == "__main__":
    main()
