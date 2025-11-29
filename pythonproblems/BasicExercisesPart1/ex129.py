from pythonproblems.functions.utils import Input


def add_leading_zeros() -> None:
    """
    This program adds leading zeroes to a string.
    Author: Gustavo Assi Alencar.
    Date:   20/11/2025.
    """

    # Step 1: Get a string from user.
    string = Input.get_string("Type a string here: ", stripped=True)

    # Step 2: Get how many zeros and which direction to add.
    amount_of_zeros = Input.get_integer_number("How many zeros: ", must_be_positive=True)
    direction = Input.get_string("Direction (left | right): ", stripped=True)

    # Step 3: Depending on which direction, use rjust or ljust.
    if direction.upper()[0] in 'RL':
        if direction.upper()[0] == 'R':
            string = string.ljust(amount_of_zeros + len(string), '0')
        elif direction.upper()[0] == 'L':
            string = string.rjust(amount_of_zeros + len(string), '0')
        print(f">>> String with zeros: {string}")
    else:
        print(f'>>> Invalid direction "{direction}". Try again...')


def main():
    add_leading_zeros()


if __name__ == "__main__":
    main()
