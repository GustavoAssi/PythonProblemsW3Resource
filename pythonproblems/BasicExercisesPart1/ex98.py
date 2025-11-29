import time


def get_system_time() -> None:
    """
    This program gets system time.
    Author: Gustavo Assi Alencar.
    Date:   13/11/2025.
    """

    # Step 1: Display system time with time module.
    print(f">>> System time: {time.ctime()}")


def main() -> None:
    get_system_time()


if __name__ == "__main__":
    main()
