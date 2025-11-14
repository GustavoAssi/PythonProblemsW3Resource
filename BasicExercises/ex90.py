import os
from utils import Input


def file_copy(source_file, destiny_file) -> None:
    """
    Procedure to copy a source file content to a destiny file.
    :param source_file:  (str) source file to copy content.
    :param destiny_file: (str) destiny file to store source file content.
    """
    with open(source_file, 'r') as source, open(destiny_file, 'w') as destiny:
        for line in source:
            destiny.write(line)


def self_replicating_program() -> None:
    """
    This program creates a copy of its own source code.
    Author: Gustavo Assi Alencar.
    Date:   13/11/2025.
    """

    # Step 1: Get a source file from user.
    source_file_input = Input.get_string("Type an path from a file: ", stripped=True)

    # Step 2: Generate a copy (if file exists).
    if os.path.exists(source_file_input):
        destiny_file_output = "copy_of_" + source_file_input.split('/')[-1]
        file_copy(source_file_input, destiny_file_output)

        # Step 3: End copy process.
        print(f">>> File copied: {destiny_file_output}")
    else:
        print(f">>> Couldn't find file: {source_file_input}")


def main() -> None:
    self_replicating_program()


if __name__ == "__main__":
    main()
