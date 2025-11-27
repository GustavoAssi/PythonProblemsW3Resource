from utils import Input


def character_frequency_counter() -> None:
	"""
	This program counts the number of occurrences of a specific character in a string.
	Author: Gustavo Assi Alencar.
	Date:   08/11/2025.
	"""

	# Step 1: Get the string.
	string_input = Input.get_string("Type a string: ")
	
	# Step 2: Get the character.
	character_input = Input.get_string("Type a character: ")

	# Step 3: Count the number of occurrences of the character in the string.
	number_of_occurrences = string_input.count(character_input)

	# Step 4: Display the result.
	cases = {
		number_of_occurrences: f"appear {number_of_occurrences} times",
		0: "doesn't appear", 
		1: "appear just once", 
	}
	print(f'>>> "{character_input}" {cases[number_of_occurrences]} in "{string_input}"')


def main() -> None:
	character_frequency_counter()


if __name__ == "__main__":
	main()
