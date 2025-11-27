from utils import Input


def odd_product_pair_checker() -> None:
    """
    This program checks whether a distinct pair of numbers whose
    product is odd is present in a sequence of integer values.
    Author: Gustavo Assi Alencar.
    Date:   25/11/2025.
    """

    # Step 1: Insert a list of integer numbers.
    numbers = Input.get_list("Type a few integer numbers: ", elements_type="int")

    # Step 2: Check in the list all the pair of numbers where the product is odd.
    n = len(numbers)
    for i in range(0, n):
        for j in range(i + 1, n):
            product = numbers[i] * numbers[j]
            if product % 2 != 0:
                print(f">>> {numbers[i]} x {numbers[j]} = {product}")


def main():
    odd_product_pair_checker()


if __name__ == "__main__":
    main()
