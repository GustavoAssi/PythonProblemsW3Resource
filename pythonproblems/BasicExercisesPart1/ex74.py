from pythonproblems.functions.utils import Input


def word_hasher() -> None:
	"""
	This program hashes a word.
	Author: Gustavo Assi Alencar.
	Date:   06/11/2025.
	"""

	# Step 1: Define a map to hash characters.
	soundex = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4, 5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2]

	# Step 2: Get the word from user.
	word = Input.get_string(">>> Type a word to be hashed: ", stripped=True).upper()

	# Step 3: Apply the hash algorithm.
	hashed_word = word[0]
	for character in word[1:]:
		index = 65 - ord(character)
		hashed_word += str(soundex[index])

	# Step 4: Display the hashed word.
	print(f">>> Hashed word: {hashed_word}")


def main() -> None:
	word_hasher()


if __name__ == "__main__":
	main()
