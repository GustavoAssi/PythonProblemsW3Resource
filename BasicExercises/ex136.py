import os
from utils import Input


def files_only_in_directory() -> None:
    """
    This program finds files and skip directories in a given directory.
    Author: Gustavo Assi Alencar.
    Date:   24/11/2025.
    """

    # Step 1: Get a directory path.
    path = Input.get_string("Type the directory path: ", stripped=True)

    # Step 2: If path exists and is a directory, print all files in this directory.
    if os.path.exists(path) and os.path.isdir(path):
        for element in os.listdir(path):
            if os.path.isfile(path + "/" + element):
                print(element)
    else:
        print(">>> Provided path neither exists nor is a directory. Try again...")


def main():
    files_only_in_directory()


if __name__ == "__main__":
    main()
