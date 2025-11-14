import os
from utils import Input


def file_size_finder() -> None:
    """
    This program gets the size of a file.
    Author: Gustavo Assi Alencar.
    Date:   13/11/2025.
    """

    # Step 1: Get file path.
    file_path = Input.get_string("Input a file path: ", stripped=True)

    # Step 2: If file exists, get the size of file.
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)

        # Step 3: Display results.
        print(f">>> File size: {file_size} Bytes")

    else:
        print(f">>> Couldn't find file in: {file_path}")


def main() -> None:
    file_size_finder()


if __name__ == "__main__":
    main()
