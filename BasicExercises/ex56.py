import fcntl
import termios
import struct


def console_dimensions() -> None:
	"""
	This program gets the height and width of the console window.
	Author: Gustavo Assi Alencar.
	Date:   04/11/2025.
	"""

	# What fuck is this?
	th, tw, hp, wp = struct.unpack("HHHH", fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack("HHHH", 0, 0, 0, 0)))
	print(f">>> th: {th}")
	print(f">>> tw: {tw}")
	print(f">>> hp: {hp}")
	print(f">>> wp: {wp}")


def main() -> None:
	console_dimensions()


if __name__ == "__main__":
	main()

