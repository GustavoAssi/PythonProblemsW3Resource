from pythonproblems.functions.utils import Input


def is_a_binary_string(string: str) -> bool:
    """
    Returns is a string is a binary string, with only zeros and ones.
    :param string: (str) the string to check if is a binary string.
    :return:       (bool) True if is a binary string, False otherwise.
    """

    return all([value in "01" for value in string])


def separate_subsequences_from_binary_string(binary_string: str) -> dict:
    """
    Returns a dictionary with the sequences of zeros and ones.
    :param binary_string: (str) a string of zeros and ones.
    :return:              (dict) a dictionary with all zeros and ones subsequences.
    """
    binary_string_encoded = ""
    index = 0
    while index < len(binary_string):
        binary_string_encoded += binary_string[index]
        if index <= len(binary_string) - 2 and binary_string[index + 1] != binary_string[index]:
            binary_string_encoded += ' '
        index += 1
    sub_sequences = binary_string_encoded.split()
    zeros = [sequence for sequence in sub_sequences if sequence.startswith('0')]
    ones = [sequence for sequence in sub_sequences if sequence.startswith('1')]

    return {"zeros": zeros, "ones": ones}


def sequences_of_zeros_and_ones_match(zeros: list, ones: list) -> bool:
    """
    Returns True if the subsequences of zeros and ones match.
    :param zeros: (list) list of a subsequence of zeros.
    :param ones:  (list) list of a subsequence of ones.
    :return:      (bool) True if all subsequences matches in length, False otherwise.
    """
    if len(zeros) != len(ones):
        return False
    else:
        for index in range(0, len(zeros)):
            if len(zeros[index]) != len(ones[index]):
                return False
        else:
            return True


def consecutive_zero_one_checker() -> None:
    """
    This program checks if every consecutive sequence of zeroes is followed by
    a consecutive sequence of ones of same length in a given string.
    Author: Gustavo Assi Alencar.
    Date:   24/11/2025.
    """

    # Step 1: Input a binary string.
    string = Input.get_string("Type a binary string: ", stripped=True)

    # Step 2: Analyse this string.
    if is_a_binary_string(string):

        # Step 3: Separate the sequence of zeros from the sequences of ones.
        sequences = separate_subsequences_from_binary_string(string)
        zeros = sequences["zeros"]
        ones = sequences["ones"]

        # Step 4: Compare the subsequences.
        if sequences_of_zeros_and_ones_match(zeros, ones):
            print(f">>> Passed")
        else:
            print(f">>> Failed")
    else:
        print("User typed a non binary string! Try again...")


def main():
    consecutive_zero_one_checker()


if __name__ == "__main__":
    main()
