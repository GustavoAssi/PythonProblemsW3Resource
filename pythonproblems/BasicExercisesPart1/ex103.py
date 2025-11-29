import os
from pythonproblems.functions.utils import Input


def extract_file_name() -> None:
    """
    This program extracts the filename from a given path.
    Author: Gustavo Assi Alencar.
    Date:   14/11/2025.
    """

    # Step 1: Get file path from user.
    file_path = Input.get_string("Type an file path: ", stripped=True)

    # Step 2: If file exists, get file name.
    if os.path.exists(file_path):
        file_path_parts = file_path.split('/')
        file_name = file_path_parts[-1]

        # Step 3: Display the results.
        print(f">>> File name: {file_name}")
    else:
        print(f"File: {file_path} does not exist!")

def main() -> None:
    extract_file_name()


if __name__ == "__main__":
    main()
