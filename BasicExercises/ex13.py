def print_here_document() -> None:
	"""
	This program prints the follwing here document.
	Author: Gustavo Assi Alencar.
	Date:   27/10/2025.
	"""

	print("""
	a string that you "don't" have to scape
	This
	is a ....... multi-line
	heredoc string --------> example
	""")


def main() -> None:
	print_here_document()


if __name__ == "__main__":
	main()