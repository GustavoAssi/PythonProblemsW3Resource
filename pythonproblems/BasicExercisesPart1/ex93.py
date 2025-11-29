def object_identity_and_type() -> None:
    """
    This program gets identity, type and value from an object.
    Author: Gustavo Assi Alencar.
    Date:   13/11/2025.
    """

    # Step 1: Set a few Python objects.
    objects = ["Python", 1,3.1415, (1, 2 ,3), {1, 2, 3}, {"name": "Python", "version": 3.12}]

    # Step 2: For each object, display identity, type and value.
    for obj in objects:
        print(f">>> Identity: {obj}")
        print(f">>> Type: {type(obj)}")
        print(f">>> Value (in memory): {id(obj)}")
        print("\n")


def main() -> None:
    object_identity_and_type()


if __name__ == "__main__":
    main()
