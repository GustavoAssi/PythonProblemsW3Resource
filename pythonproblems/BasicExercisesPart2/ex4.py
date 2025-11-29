from pythonproblems.functions.utils import Input


def get_tripplets_with_sum_equal_to_zero(numbers: list):
    """
    Returns a tuple with a tripplet of values whose sum is equal to zero.
    :param numbers: (list) a few integer numbers.
    """
    # TODO: Try refactor this function to be more efficient than this O(n³) algorithm.
    tripplets = []
    n = len(numbers)
    for i_index in range(0, n):
        for j_index in range(i_index + 1, n):
            for k_index in range(j_index + 1, n):
                tripplet = [numbers[i_index], numbers[j_index], numbers[k_index]]
                tripplet.sort()  # In this case is easy sort an array with 3 values.
                if tripplet not in tripplets and sum(tripplet) == 0:
                    tripplets.append(tripplet)

    return tripplets


def zero_sum_triplets() -> None:
    """
    This program identifies unique triplets whose
    three elements sum to zero from an array of n integers.
    Author: Gustavo Assi Alencar.
    Date:   26/11/2025.
    """

    # Step 1: Get a list of integers.
    numbers = Input.get_list("Type a few integer numbers: ", elements_type="int")

    # Step 2: Start the O(n³) algorithm to get the tripplets.
    tripplets = get_tripplets_with_sum_equal_to_zero(numbers)

    # Step 3: Display the tripplets.
    print(f"Tripplets: ")
    for tripplet in tripplets:
        print(tripplet)


def main() -> None:
    zero_sum_triplets()


if __name__ == "__main__":
    main()
