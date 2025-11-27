def special_characters_in_string() -> None:
    """
    This program defines a string containing special characters in various forms.
    Author: Gustavo Assi Alencar.
    Date:   13/11/2025.
    """

    # Step 1: Just print many forms of strings with special characters.
    # Hint: Use raw strings, a raw string ignores scape characters like \n, \t, \\, etc.
    print(r"\#{'}${\"}@/")
    print(r"\#{'}${\"}@/")
    print(r"""\#{'}${"}@/""")
    print(r'\#{'"'"'}${"}@/')
    print(r'''\#{'}${"}@/''')


def main() -> None:
    special_characters_in_string()


if __name__ == "__main__":
    main()
