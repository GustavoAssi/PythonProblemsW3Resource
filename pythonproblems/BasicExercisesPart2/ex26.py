from pythonproblems.functions.utils import Input


def absolute_pairwise_difference() -> None:
    """
    This program computes the summation of the absolute difference of all distinct
    pairs in a given array (non-decreasing order).x
    Author: Gustavo Assi Alencar.
    Date:   08/12/2025.
    """

    # Step 1: Get an array of integer numbers from user.
    array = Input.get_list("Type a few integer numbers: ", elements_type="int")

    # Step 2: Compute the sum of absolute difference of distinct pairs.
    numbers_set = list(set(array))
    set_length = len(numbers_set)
    sum_value = 0
    for i_index in range(0, set_length):
        for j_index in range(i_index + 1, set_length):
            abs_diff = abs(numbers_set[i_index] - numbers_set[j_index])
            print(f"|{numbers_set[i_index]} - {numbers_set[j_index]}| = {abs_diff}")
            sum_value += abs_diff

    # Step 3: Display the result.
    print(f">>> Summation of all distinct pairs: {sum_value}")


def main() -> None:
    absolute_pairwise_difference()


if __name__ == "__main__":
    main()
