def extract_directory_pair() -> None:
    """
    This program extracts a single key-value pair from a dictionary into variables.
    Author: Gustavo Assi Alencar.
    Date:   24/11/2025.
    """

    # Step 1: Set up a dictionary object.
    dictionary = {"Language": "Python"}

    # Step 2: Use items() to set variables.
    (language, python), = dictionary.items()

    # Step 3: Display the results.
    print(f">>> {language}: {python}")


def main():
    extract_directory_pair()


if __name__ == "__main__":
    main()
