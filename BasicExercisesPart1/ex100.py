import socket


def get_host_name() -> None:
    """
    This program gets the name of the host on which routine is running.
    Author: Gustavo Assi Alencar.
    Date:   13/11/2025.
    """

    # Step 1: Display username using socket module.
    print(f">>> Username: {socket.gethostname()}")


def main() -> None:
    get_host_name()


if __name__ == "__main__":
    main()
