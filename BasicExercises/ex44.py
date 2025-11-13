import site
import pkg_resources


def python_site_packages_locator() -> None:
	"""
	This program locates Python site packages.
	Author: Gustavo Assi Alencar.
	Date:   02/11/2025.
	"""

	# Step 1: Using site module, get site packages path.
	site_packages_paths = site.getsitepackages()

	# Step 2: Display site packages path and the packages.
	print(f"All site packages paths: ")
	for path in site_packages_paths:
		print(f"\t* {path}")
	
	for dist in pkg_resources.working_set:
		dist_info = str(dist).split()
		package_name, version = dist_info[0], dist_info[1]
		print(f"{package_name}: {version}")


def main() -> None:
	python_site_packages_locator()


if __name__ == "__main__":
	main()
