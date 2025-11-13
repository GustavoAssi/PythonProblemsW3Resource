from utils import Input


def pressure_unit_converter() -> None:
	"""
	This program converts pressure in kilopascals to: 
		* pounds per square inch; 
		* a millimeter of mercury (mmHg); 
		* atmosphere pressure.
	Author: Gustavo Assi Alencar.
	Date:   05/11/2025.
	"""

	# Step 1: Get the pressure in kilopascals.
	kilopascals_pressure = Input.get_float_number("Input pressure in kilopascals: ")

	# Step 2: Convert for other units: pounds per inch squared, mmHg and atm.
	pounds_per_inch_squared_pressure = kilopascals_pressure * 0.145038
	militer_of_mercury_pressure = kilopascals_pressure * 7.50062
	atmosphere_pressure = kilopascals_pressure * 0.00986923
	
	# Step 3: Display the results.
	print(f">>> {kilopascals_pressure} kPa = {pounds_per_inch_squared_pressure:.3f} lb/in² (psi)")
	print(f">>> {kilopascals_pressure} kPa = {militer_of_mercury_pressure:.3f} mmHg")
	print(f">>> {kilopascals_pressure} kPa = {atmosphere_pressure:.3f} atm")


def main() -> None:
	pressure_unit_converter()


if __name__ == "__main__":
	main()
