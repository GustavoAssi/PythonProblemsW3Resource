import socket


def find_local_IPs() -> None:
	"""
	This program finds local IP addresses using Python's stdlib.
	Author: Gustavo Assi Alencar.
	Date:   04/11/2025.
	"""

	# Step 1: Get the local hostname.
	local_hostname = socket.gethostname()

	# Step 2: Get a list of IP addresses associated with the hostname.
	ip_addresses = socket.gethostbyname_ex(local_hostname)[2]

	# Step 3: Filter out loopback addresses (IPs starting with "127.").
	filtered_ips = [ip for ip in ip_addresses if not ip.startswith("127.")]

	# Step 4: Extract the first IP address (if available) from the filtered list.
	first_ip = filtered_ips[:1] if len(filtered_ips) > 0 else ip_addresses

	# Step 5: Print the obtained IP address to the console.
	print(first_ip)


def main() -> None:
	find_local_IPs()


if __name__ == "__main__":
	main()
