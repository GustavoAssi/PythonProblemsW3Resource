from utils import Input


def vowel_tester() -> None:
	"""
	This program tests wheter a passed letter is a vowel or not.
	Author: Gustavo Assi Alencar.
	Date:   30/10/2025.
	"""

	# Step 1: Get the letter from user.
	letter = Input.get_string("Type a letter: ", stripped=True)

	if len(letter) == 1 and letter.isalpha():

		# Step 2: Check wheter is a vowel or not.
		if letter.lower() in 'aeiou':
			print("User typed a vowel!")
		else:
			print("User typed a consoant!")
	else:
		print("User didn't typed a letter...") 



def main() -> None:
	vowel_tester()


if __name__ == "__main__":
	main()