import itertools
from pythonproblems.functions.utils import Input


def sum_of_digits_combinations() -> None:
    """
    This program reads n digits (given) chosen from 0 to 9 and prints the 
    number of combinations where the sum of the digits equals another given number (s). 
    Author: Gustavo Assi Alencar.
    Date:   25/12/2025.
    """

    # Step 1: Get the number of digits and target value.
    number_of_digits = Input.get_integer_number("Type the number of digits: ", must_be_positive=True)
    target_value = Input.get_integer_number("Type the target value: ", must_be_positive=True)

    # Step 2: Get the combinations of numbers where the sum is equal to the target.
    generators = (range(10) for _ in range(number_of_digits))
    combinations = []
    for values in itertools.product(*generators):
        combination = sorted(values)
        if combination not in combinations and sum(combination) == target_value:
            combinations.append(combination)

    # Step 3: Display the results:
    for combination in combinations:
        for index in range(number_of_digits):
            if index != number_of_digits - 1:
                print(f"{combination[index]} + ", end="")
            else:
                print(f"{combination[index]} = {target_value}")


def main() -> None:
    sum_of_digits_combinations()


if __name__ == "__main__":
    main()
