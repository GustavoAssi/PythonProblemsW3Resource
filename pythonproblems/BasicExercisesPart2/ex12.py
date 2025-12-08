from math import factorial
from pythonproblems.functions.utils import Input


def generate_permutations(numbers):
    """
    This function returns the permutations from an array of numbers
    using backtrack implementation.
    """

    # TODO: study better this type of algorithm. Let's call it "Combinatoric Algorithms".
    result = []
    n = len(numbers)
    used_elements = [False for _ in range(n)]

    def backtrack(current_permutation):
        if len(current_permutation) == n:
            result.append(current_permutation.copy())
            return

        for index in range(0, n):
            if not used_elements[index]:
                used_elements[index] = True
                current_permutation.append(numbers[index])
                backtrack(current_permutation)
                current_permutation.pop()
                used_elements[index] = False

    backtrack([])
    return result


def list_permutations_generator() -> None:
    """
    This program generates a list of all possible permutations
    from a given collection of distinct numbers.
    Author: Gustavo Assi Alencar.
    Date:   29/11/2025.
    """

    # Step 1: Get the numbers from user.
    numbers = Input.get_list("Input a list of distinct numbers: ")

    # Step 2: Start the algorithm to get all permutations.
    permutations = generate_permutations(numbers)
    assert len(permutations) == factorial(len(numbers)), "Number of permutations is incorrect"

    # Step 3: Display the result.
    for permutation in permutations:
        print(permutation)


def main() -> None:
    list_permutations_generator()


if __name__ == "__main__":
    main()
