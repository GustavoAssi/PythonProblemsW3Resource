from pythonproblems.functions.utils import Input


def parallelogram_validator() -> None:
    """
    This program reads the two adjoining sides and the diagonal of a parallelogram 
    and checks whether the parallelogram is a rectangle or a rhombus.
    Author: Gustavo Assi Alencar.
    Date:   25/12/2025.
    """

    # Step 1: Get adjoining sides and diagonal values.
    l1 = Input.get_float_number("Input 1º side of quadrilateral (positive float): ", must_be_positive=True)
    l2 = Input.get_float_number("Input 2º side of quadrilateral (positive float): ", must_be_positive=True)
    dg = Input.get_float_number("Input the diagonal of quadrilateral (positive float): ", must_be_positive=True)

    # Step 2: Classify the quadrilateral according with the angle between the sides.
    cossine_theta = ((l1**2 + l2**2) - dg**2) / (2*l1*l2)
    if cossine_theta == 0:
        print(">>> Is a rectangle")
    elif cossine_theta != 0 and l1 == l2:
        print(">>> Is a rhombus")
    elif cossine_theta != 0 and l1 != l2:
        print(">>> Is a parallelogram")
    else:
        print("Is not a quadrilateral")


def main() -> None:
    parallelogram_validator()


if __name__ == "__main__":
    main()
