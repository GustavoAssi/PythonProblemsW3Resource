import os
import sys
import time


def clear_terminal() -> None:
    """
    This program clears the screen or terminal.
    Author: Gustavo Assi Alencar.
    Date:   13/11/2025.
    """

    # Step 1: Display something in terminal.
    os.system("ls")

    # Step 2: Wait for 5 seconds.
    time.sleep(5)

    # Step 3: Clear terminal screen.
    if sys.stdout.isatty():
        os.system("clear")
    else:
        print("\n" * 100)


def main() -> None:
    clear_terminal()


if __name__ == "__main__":
    main()
