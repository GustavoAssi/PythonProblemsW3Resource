import os


def process_group_and_user_ids() -> None:
    """
    This program gets the effective group id, effective user id, real group id and list of supplemental group ids.
    All of them associated with the current process.
    Author: Gustavo Assi Alencar.
    Date:   14/11/2025.
    """

    # Step 1: Get the effective group ID and print it.
    print("Effective group id: ", os.getegid())

    # Step 2: Get the effective user ID and print it.
    print("Effective user id: ", os.geteuid())

    # Step 3: Get the real group ID and print it.
    print("Real group id: ", os.getgid())

    # Step 4: Get the list of supplemental group IDs and print them.
    print("List of supplemental group ids: ", os.getgroups())



def main() -> None:
    process_group_and_user_ids()


if __name__ == "__main__":
    main()
