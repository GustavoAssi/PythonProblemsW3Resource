def string_memory_location_test() -> None:
    """
    This program proves that two string variables of the same value point to the same memory location.
    Author: Gustavo Assi Alencar.
    Date:   15/11/2025.
    """

    # Step 1: Set up a string value in 2 different variables.
    string1 = "Python is awesome!"
    string2 = "Python is awesome!"

    # Step 2: Display location in memory.
    location1 = hex(id(string1))
    location2 = hex(id(string2))

    print(f'>>> location of string 1 = "{string1}": {location1}')
    print(f'>>> location of string 2 = "{string2}": {location2}')

    # Step 3: Prove that the memory locations are the same.
    if location1 == location2:
        print(f"The locations in memory are the same")


def main() -> None:
    string_memory_location_test()


if __name__ == "__main__":
    main()
