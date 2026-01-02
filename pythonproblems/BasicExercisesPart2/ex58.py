from pythonproblems.functions.utils import Input


def restore_compressed_string() -> None:
    """
    This program restores the original string by entering the compressed string with this rule.
    Author: Gustavo Assi Alencar.
    Date:   28/12/2025.
    """

    # Step 1: Get the compressed string.
    string = Input.get_string("Input the compressed string: ", stripped=True)

    # Step 2: Restore the string.
    while "#" in string:
        try:
            hash_index = string.index('#')
            next_char = string[hash_index + 1]
            if next_char.isnumeric:
                frequency = int(next_char)
                repeated_char = string[hash_index + 2]
                string = string[:hash_index] + frequency * repeated_char + string[hash_index + 3:]
        except IndexError:
            pass

    # Step 3: Display the result.
    print(f">>> Original text: {string}")


def main() -> None:
    restore_compressed_string()


if __name__ == "__main__":
    main()
