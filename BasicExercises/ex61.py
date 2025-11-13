from utils import Input


def feet_to_other_units() -> None:
	"""
	This program converts the distance (in feet) to inches, yards, and miles.
	Author: Gustavo Assi Alencar.
	Date:   04/11/2025.
	"""

	# Step 1: Get the distance in feet?
	distance_in_feet = Input.get_float_number("Type the distance in feet: ", must_be_positive=True)

	# Step 2: Convert the distance in inches, yards and miles.
	distance_in_inches = 12 * distance_in_feet
	distance_in_yards = distance_in_feet / 3
	distance_in_miles = distance_in_feet / 5280

	# Step 3: Display the results.
	print(f">>> {distance_in_feet:.3f} feet = {distance_in_inches:.4f} inches")
	print(f">>> {distance_in_feet:.3f} feet = {distance_in_yards:.4f} yards")
	print(f">>> {distance_in_feet:.3f} feet = {distance_in_miles:.4f} miles")


def main() -> None:
	feet_to_other_units()


if __name__ == "__main__":
	main()
