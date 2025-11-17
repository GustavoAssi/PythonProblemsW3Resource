import os.path
import time


def file_properties_retriever() -> None:
    """
    This program retrieves a file properties.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: Print file properties.
    print(f">>> file:          {__file__}")
    print(f">>> access time:   {time.ctime(os.path.getatime(__file__))}")
    print(f">>> modified time: {time.ctime(os.path.getmtime(__file__))}")
    print(f">>> change time:   {time.ctime(os.path.getctime(__file__))}")
    print(f">>> size:          {os.path.getsize(__file__)} bytes")


def main() -> None:
    file_properties_retriever()


if __name__ == "__main__":
    main()
