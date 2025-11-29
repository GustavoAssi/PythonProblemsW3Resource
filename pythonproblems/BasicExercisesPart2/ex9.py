from importlib.metadata import distributions


def locally_intalled_modules() -> None:
    """
    This program gets a list of locally installed Python modules.
    Author: Gustavo Assi Alencar.
    Date:   26/11/2025.
    """

    # Step 1: Get locally packages using metadata from importlib.
    for dist in distributions():
        print(f"{dist.metadata['name']} == {dist.version}")


def main() -> None:
    locally_intalled_modules()


if __name__ == "__main__":
    main()
