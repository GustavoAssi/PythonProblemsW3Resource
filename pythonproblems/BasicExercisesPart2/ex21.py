from pythonproblems.functions.utils import Input


def notes_count_from_amount() -> None:
    """
    This program finds the number of notes
    Samples of notes: 10, 20, 50, 100, 200, 500 against an amount.
    Author: Gustavo Assi Alencar.
    Date:   08/12/2025.
    """

    # Step 1: Get the amount from user.
    amount = Input.get_integer_number("Type a amount of money: ", must_be_positive=True)

    # Step 2: find the number of notes.
    notes_counter = {"$500": 0, "$200": 0, "$100": 0, "$50": 0, "$20": 0, "$10": 0, "$5": 0, "$1": 0}
    notes_values = [500, 200, 100, 50, 20, 10, 5, 1]
    for note in notes_values:
        notes_counter[f"${note}"] = amount // note
        amount %= note

    for note_sample, amount in notes_counter.items():
        print(f">>> {note_sample}: {amount} notes")

    print(f">>> Total: {sum(notes_counter.values())} notes")


def main() -> None:
    notes_count_from_amount()


if __name__ == "__main__":
    main()
