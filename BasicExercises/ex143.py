import struct


def shell_bit_mode_detector() -> None:
    """
    This program determines if the Python shell is executing in 32-bit or 64-bit mode on the operating system.
    Author: Gustavo Assi Alencar.
    Date:   24/11/2025.
    """

    # Step 1: Use calcsize from struct module to get os size.
    print(f">>> {struct.calcsize('P') * 8} bits")


def main():
    shell_bit_mode_detector()


if __name__ == "__main__":
    main()
