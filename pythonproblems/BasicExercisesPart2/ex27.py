from pythonproblems.functions.utils import Input


def progression_type_and_next() -> None:
    """
    This program generates a Arithmetic or Geometric progression of numbers.
    Author: Gustavo Assi Alencar.
    Date:   08/12/2025.
    """

    # Step 1: Get first term, ratio, number of terms and sequence type.
    first_term = Input.get_integer_number("Type the first term of the sequence: ")
    ratio = Input.get_integer_number("Type the ratio value of the sequence: ")
    number_of_terms = Input.get_integer_number("Type the number of terms: ", must_be_positive=True)
    sequence_type = Input.get_character("Type the type of sequence (A - Arithmetic Progression | G - Geometric Progression): ")

    # Step 2: Generate the sequence.
    current_term = first_term
    sum_of_values = 0
    for index in range(number_of_terms):
        sum_of_values += current_term
        if index == number_of_terms - 1:
            print(f"{current_term}")
        else:
            print(f"{current_term} --> ", end="")

        if sequence_type == "A":
            current_term += ratio
        elif sequence_type == "G":
            current_term *= ratio
    print(f">>> sum of values: {sum_of_values}")


def main() -> None:
    progression_type_and_next()


if __name__ == "__main__":
    main()
