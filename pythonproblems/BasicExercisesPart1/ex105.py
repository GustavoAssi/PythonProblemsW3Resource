import os


def user_enviroment_retriever() -> None:
    """
    This program gets user enviroemnt.
    Author: Gustavo Assi Alencar.
    Date:   14/11/2025.
    """

    # Step 1: Display user enviroment using os module.
    for k, v in os.environ.items():
        print(f">>> {k} : {v}")


def main() -> None:
    user_enviroment_retriever()


if __name__ == "__main__":
    main()
