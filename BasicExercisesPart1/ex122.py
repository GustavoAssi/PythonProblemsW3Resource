def empty_variable_without_deletion() -> None:
    """
    This program empties a variable without destroying it.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: Set a list of objects.
    objects = [
        "Python",
        42,
        3.1415,
        {1, 2, 3},
        [4, 5, 6],
        ("Python", "is", "a", "awesome", "language"),
        {"The Beatles": "Revolver", "Michael Jackson": "Bad"}
    ]

    # Step 2: Empty them! To empty an object, just create an instance from object type.
    for obj in objects:
        print(f">>> Original object: {obj}")
        print(f">>> Empty version: {type(obj)()}\n")


def main() -> None:
    empty_variable_without_deletion()


if __name__ == "__main__":
    main()
