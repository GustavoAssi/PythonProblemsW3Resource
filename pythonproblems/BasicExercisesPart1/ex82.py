from pythonproblems.functions.utils import Input


def is_int(value) -> bool:
	"""
	Returns if a value is int or not.

	:param value: any object to check if is int.
	:return: True or False.
	"""
	return "int" in str(type(value))


def sum_for_tuple(tuple_input: tuple) -> int:
	"""
	Returns the sum from tuple values, since all values are integers.
	"""
	
	if all([is_int(value) for value in list(tuple_input)]):
		return sum(tuple_input)
	return 0


def sum_for_list(list_input: list) -> int:
	"""
	Returns the sum from list values, since all values are integers.
	"""
	
	if all([is_int(value) for value in list_input]):
		return sum(list_input)
	return 0


def sum_for_dictionary(dict_input: dict) -> int:
	"""
	Returns the sum from dictionary values, since all values are integers.
	"""

	if all([is_int(value) for value in list(dict_input.values())]):
		return sum(list(dict_input.values()))
	return 0


def sum_for_set(set_input: set) -> int:
	"""
	Returns the sum from set values, since all values are integers.
	"""
	
	if all([is_int(value) for value in set_input]):
		return sum(set_input)
	return 0



def sum_of_container_items() -> None:
	"""
	This program calculates the sum of all items of a container (tuple, list, set, dictionary).
	Author: Gustavo Assi Alencar.
	Date:   08/11/2025.
	"""

	# Step 1: Insert an iterable.
	iterable = Input.get_string("Type an iterable (tuple, list, set, dictionary): ", stripped=True)

	try: 
		# Step 2: Try to get iterable type.
		result = {}
		exec(f"iterable_value = {iterable}", {}, result)
		iterable_value = result["iterable_value"]
		exec(f"iterable_type = str(type({iterable_value}))", {}, result)
		iterable_type = result["iterable_type"]

		# Step 3: Display iterable type and sum of values.
		types = {
			"<class 'tuple'>": {"message": "User typed a tuple",      "sum_function": sum_for_tuple}, 
			"<class 'list'>":  {"message": "User typed a list",       "sum_function": sum_for_list}, 
			"<class 'dict'>":  {"message": "User typed a dictionary", "sum_function": sum_for_dictionary},  
			"<class 'set'>":   {"message": "User typed a set",        "sum_function": sum_for_set}, 
		}

		print(f">>> Iterable type: {types[iterable_type]["message"]}")
		print(f">>> Sum of values type: {types[iterable_type]["sum_function"](iterable_value)}")

	except SyntaxError:
		print(f">>> Unknown type for: {iterable}")


def main() -> None:
	sum_of_container_items()


if __name__ == "__main__":
	main()
