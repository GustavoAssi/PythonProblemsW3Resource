from utils import Input


def bmi_calculator() -> None:
	"""
	This program calculates the body mass index.
	Author: Gustavo Assi Alencar.
	Date:   05/11/2025.
	"""

	# Step 1: Get weight (kg) and height (m) from user.
	weight = Input.get_float_number("Type your weight (kg): ", must_be_positive=True)
	height = Input.get_float_number("Type your height  (m): ", must_be_positive=True)

	if weight == 0 or height == 0:
		print("Failed to calculate BMI: user input 0 for weight or height") 
	else:
		
		# Step 2: Calculate BMI = weight / height² (kg/m²).
		bmi = weight / (height ** 2)

		# Step 3: Display the results.
		print(f">>> Your BMI (Body Mass Index): {bmi:.3}")
		print(">>> According to WHO (World Health Organization): ", end="")
		if bmi < 18.5:
			print("You're underweight")
		elif  18.5 <= bmi < 24.9:
			print("You're in normal weight range")
		elif 24.9 <= bmi < 29.9:
			print("You're overweight")
		else:
			print("You're obese")


def main() -> None:
	bmi_calculator()


if __name__ == "__main__":
	main()
