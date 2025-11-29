from pythonproblems.functions.utils import Input


def create_bytearray_from_list() -> None:
    """
    This program creates a bytearray from a list.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: Get an array from user.
    array = Input.get_list("Type a few integer numbers: ", elements_type="int")

    # Step 2: Create the bytearray.
    byte_array = bytearray(array)

    # Step 3: Display the byte array.
    print(f">>> byte array: {byte_array}")


def main() -> None:
    create_bytearray_from_list()


if __name__ == "__main__":
    main()
