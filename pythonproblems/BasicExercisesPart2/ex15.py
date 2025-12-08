from pythonproblems.functions.utils import Input


def operator_priority_checker() -> None:
    """
    This program checks the priority of the four operators (+, -, *, /).
    Author: Gustavo Assi Alencar.
    Date:   29/11/2025.
    """

    # Step 1: Define some operators, parenthesis and operator priorities.
    priority = {'+': 0, '-': 0, '*': 1, '/': 1, '(': 2, ')': 2}

    def test_priority(op_1, op_2):
        return priority[op_1] >= priority[op_2]

    # Step 2: Get from user the operators.xxx
    operator_1 = Input.get_character("Type the 1º operator (+-/*): ")
    operator_2 = Input.get_character("Type the 2º operator (+-/*): ")

    # Step 3: Compare the priorities.
    try:
        if test_priority(operator_1, operator_2):
            print(f'"{operator_1}" has more or equal priority than "{operator_2}"')
        else:
            print(f'"{operator_1}" has less priority than "{operator_2}"')
    except KeyError:
        print(f"Some of the operations does not exist: {operator_1} or {operator_2}")


def main() -> None:
    operator_priority_checker()


if __name__ == "__main__":
    main()
