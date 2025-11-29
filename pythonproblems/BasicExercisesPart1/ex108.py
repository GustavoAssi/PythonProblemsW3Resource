import os.path
from pythonproblems.functions.utils import Input


def file_or_directory_path_finder() -> None:
    """
    This program finds the path to a file or directory when you encounter a path name.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: Get a dir from user.
    directory_path = Input.get_string("Type an directory path: ", stripped=True)

    # Step 2: For all files in this directory, apply file, path and link finder.
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        for file in os.listdir(directory_path):
            print(f">>> file: {file}")
            print(f">>> Absolute:      {os.path.isabs(file)}")
            print(f">>> Is file?       {os.path.isfile(file)}")
            print(f">>> Is dir?        {os.path.isdir(file)}")
            print(f">>> Is link?       {os.path.islink(file)}")
            print(f">>> file exists?   {os.path.exists(file)}")
            print(f">>> link exists?   {os.path.lexists(file)}")
            print("\n")
    else:
        print(f"Path {directory_path} doesn't exist or is not a directory path.")


def main() -> None:
    file_or_directory_path_finder()


if __name__ == "__main__":
    main()
