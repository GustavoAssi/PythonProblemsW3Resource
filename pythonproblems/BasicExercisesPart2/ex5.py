def three_digit_combinations() -> None:
    """
    This program make combinations of 3 digits.
    Author: Gustavo Assi Alencar.
    Date:   26/11/2025.
    """

    # I think I don't understand the goal of this exercise.
    # Step 1: Make the combinations using zfill.
    for num in range(1000):
        num = str(num).zfill(3)
        print(num)


def main() -> None:
    three_digit_combinations()


if __name__ == "__main__":
    main()
