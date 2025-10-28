from math import pi


def sphere_volume():
	"""
	This program calculates the volume from a sphere given the sphere radius.
	Author: Gustavo Assi Alencar.
	Date:   27/10/2025.
	"""

	# Step 1: Get sphere radius value from user.
	sphere_radius = float(input("Type the sphere radius: "))

	# Step 2: Calculate sphere volume.
	sphere_volume = (4/3) * pi * pow(sphere_radius, 3)
	
	# Step 3: Display the result.
	print(f">>> Sphere volume: {sphere_volume:.3f}")


def main():
	sphere_volume()


if __name__ == "__main__":
	main()