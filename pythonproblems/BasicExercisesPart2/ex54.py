from pythonproblems.functions.utils import Input


def regions_from_straight_lines() -> None:
    """
    This program creates the maximum number of regions obtained by drawing n given straight lines.
    Author: Gustavo Assi Alencar.
    Date:   28/12/2025.
    """

    # Step 1: Get a value for n.
    n = Input.get_integer_number("Type the number of straight lines: ", must_be_positive=True)

    # Step 2: Consider the math formula for number of planes: f(n) = (n² + n + 2)/2.
    fn = (n**2 + n + 2) // 2
    print(f">>> The max number of planes are: {fn} planes")


def main() -> None:
    regions_from_straight_lines()


if __name__ == "__main__":
    main()
