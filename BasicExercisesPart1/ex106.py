import os
from utils import Input


def path_extension_splitter() -> None:
    """
    This program divides a path by the extension separator.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: Get an path by the user.
    file_path = Input.get_string("Type a file path: ", stripped=True)

    # Step 2: Split the file by extension.
    file_name, file_extension = "", ""
    if os.path.exists(file_path):
        file_path_parts = file_path.split(".")
        file_path_founded, file_extension = tuple(file_path_parts)
        file_name = file_path_founded.split("/")[-1]

    # Step 3: Display the results.
    print(f">>> ({file_name}, .{file_extension})")

def main() -> None:
    path_extension_splitter()


if __name__ == "__main__":
    main()
