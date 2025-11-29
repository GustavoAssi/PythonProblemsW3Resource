import socket
from pythonproblems.functions.utils import Input


def ip_address_validator() -> None:
    """
    This program validates an IP address.
    Author: Gustavo Assi Alencar.
    Date:   24/11/2025.
    """

    # Step 1: Get an IP address.
    address = Input.get_string("Type an IP address: ", stripped=True)

    # Step 2: Call inet_aton() function from socket module, if works, IP is valid, and invalid otherwise.
    # TODO: Try to implement the same logic using regular expressions (regex).
    try:
        socket.inet_aton(address)
        print(">>> IP is valid")
    except socket.error:
        print(">>> IP is invalid")


def main():
    ip_address_validator()


if __name__ == "__main__":
    main()
