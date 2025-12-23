from pythonproblems.functions.utils import Input


def sequence(n: int) -> int:
    """
    Returns the nth term from the sequence.
    :param n: the nth position from the sequence.
    """
    if n == 1 or n == 2 or n == 3 or n == 4:
        return 1
    return sequence(n - 1) + sequence(n - 2) + sequence(n - 3) + sequence(n - 4)


def nth_member_of_sequence() -> None:
    """
    This program creates a sequence where the first four members of the sequence are equal to one.
    Each successive term of the sequence is equal to the sum of the four previous ones.
    The goal is find the Nth member of the sequence.
    Author: Gustavo Assi Alencar.
    Date:   08/12/2025.
    """

    # Step 1: Get the nth position of the sequence.
    n = Input.get_integer_number("Type a value of n: ", must_be_positive=True)

    # Step 2: Use the recursive function to get the nth term of the sequence.
    print(f">>> {sequence(n)}")


def main() -> None:
    nth_member_of_sequence()


if __name__ == "__main__":
    main()
