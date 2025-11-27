from utils import Input


def integer_fits_in_64_bits() -> None:
    """
    This program checks whether an integer fits in 64 bits.
    Author: Gustavo Assi Alencar.
    Date:   20/11/2025.
    """

    # Step 1: Get an integer from user.
    integer = Input.get_integer_number("Type an integer number: ")

    # Step 2: Use bitlength to check if integer fits in 64 bits.
    bit_length = integer.bit_length()
    print(f">>> Number bit length: {bit_length}")
    if bit_length < 64:
        print("Number fits in 64 bits")
    else:
        print("Number doesn't fit in 64 bits")


def main():
    integer_fits_in_64_bits()


if __name__ == "__main__":
    main()
