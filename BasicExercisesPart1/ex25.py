from utils import Input


def value_in_group_tester() -> None:
	"""
	This program checks whether a specific value is contained within a group of values.
	Author: Gustavo Assi Alencar.
	Date:   30/10/2025.
	"""

	# Step 1: Get group members from user.
	group = Input.get_string("Type the group members (comma-separated): ")
	group_members = [member.strip() for member in group.split(',')]

	# Step 2: Get from user the value to be tested.
	value = Input.get_string("Type a value: ", stripped=True)

	# Step 3: Check if value is part of the group.
	if value in group_members:
		print("Value is part from the group!")
	else:
		print("Value isn't from the group!")


def main() -> None:
	value_in_group_tester()


if __name__ == "__main__":
	main()