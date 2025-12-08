from pythonproblems.functions.utils import Input


def three_array_sum_combinations() -> None:
    """
    This program checks the sum of three elements (each from an array)
    from three arrays is equal to a target value.
    Author: Gustavo Assi Alencar.
    Date:   29/11/2025.
    """

    # Step 1: Get the lists from user.
    while True:
        list_1 = Input.get_list("Type the 1º list of integer numbers: ", elements_type="int")
        list_2 = Input.get_list("Type the 2º list of integer numbers: ", elements_type="int")
        list_3 = Input.get_list("Type the 3º list of integer numbers: ", elements_type="int")

        if len(list_1) == len(list_2) == len(list_3):
            break

    # Step 2: Get a target value.
    target = Input.get_integer_number("Type an integer target: ")

    # Step 3: Start algorithm.
    for e1 in list_1:
        for e2 in list_2:
            for e3 in list_3:
                if e1 + e2 + e3 == target:
                    print(f"{e1} + {e2} + {e3} = {target}")


def main() -> None:
    three_array_sum_combinations()


if __name__ == "__main__":
    main()
