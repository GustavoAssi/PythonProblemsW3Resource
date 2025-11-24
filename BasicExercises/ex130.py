import json


def double_quotes_string_display() -> None:
    """
    This program uses double quotes to display strings.
    Author: Gustavo Assi Alencar.
    Date:   20/11/2025.
    """

    # Step 1: Set a simple dictionary structure in Python language.
    dictionary = {'Language': 'Python', 'Version': '3.12'}

    # Step 2: Use dumps from json module to return json in string format.
    json_string = json.dumps(dictionary)

    # Step 3: Compare objects.
    print(f">>> Dictionary: {dictionary}")
    print(f">>> JSON in string format: {json_string}")


def main():
    double_quotes_string_display()


if __name__ == "__main__":
    main()
