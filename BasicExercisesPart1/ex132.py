import os


def list_home_directory() -> None:
    """
    This program lists the home directory without an absolute path.
    Author: Gustavo Assi Alencar.
    Date:   20/11/2025.
    """

    # Step 1: Just display home path using os module.
    print(f">>> Home path: {os.path.expanduser('~')}")


def main():
    list_home_directory()


if __name__ == "__main__":
    main()
