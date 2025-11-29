import os
from pythonproblems.functions.utils import Input


def wildcard_file_lister() -> None:
    """
    This program makes file lists from the current directory using a wildcard.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: Get the directory path.
    directory_path = Input.get_string("Type the directory path: ", stripped=True)

    # Step 2: Get the wildcard (*, ? or []) with file extension.
    wildcard = Input.get_string("Type the wildcard (*, ? or []): ", stripped=True)
    file_extension = Input.get_string("Type the file extension: ", stripped=True)

    # Step 3: Show the list according with the wildcard and file extension.
    if os.path.exists(directory_path):
        os.system(f"ls {wildcard}{file_extension}")
    else:
        print(f"Couldn't find directory in: {directory_path}")


def main() -> None:
    wildcard_file_lister()


if __name__ == "__main__":
    main()
