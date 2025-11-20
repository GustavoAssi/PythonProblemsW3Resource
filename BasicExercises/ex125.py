from utils import Input


def sum_collection_counts() -> None:
    """
    This program sum all counts in a collection.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: Get a list from user.
    collection = Input.get_list("Input a list of objects: ")

    # Step 2: Count the elements.
    print(f">>> collection = {collection}")
    print(f">>> number of elements: {len(collection)}")


def main() -> None:
    sum_collection_counts()


if __name__ == "__main__":
    main()
