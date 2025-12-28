from pythonproblems.functions.utils import Input


def swap_python_and_java() -> None:
    """
    This program replaces a string "Python" with "Java" and "Java" with "Python" in a given string.
    Author: Gustavo Assi Alencar.
    Date:   25/12/2025.
    """

    # Step 1: Get an text with "Python" and "Java".
    text = Input.get_string('Type a text using words "Python" and "Java": ')

    # Step 2: Swap the words in text.
    text = text.replace("Python", "<java>").replace("Java", "<python>")
    text = text.replace("<java>", "Java").replace("<python>", "Python")
    
    # Step 3: Display result.
    print(f">>> {text}")


def main() -> None:
    swap_python_and_java()


if __name__ == "__main__":
    main()
