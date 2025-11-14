from http.client import HTTPConnection
from utils import Input


def url_content_printer():
    """
    This program access and prints a URL's content to the console.
    Author: Gustavo Assi Alencar.
    Date:   14/11/2025.
    """

    # Step 1: Get an url from user.
    url = Input.get_string("Input an URL: ", stripped=True)
    url = url.replace("https://", "")
    url = url.replace("http://", "")
    url = url.replace("/", "")

    try:
        # Step 2: Stablish a connection.
        connection = HTTPConnection(url)

        # Step 3: Send a request.
        connection.request("GET", "/")
        result = connection.getresponse()

        # Step 4: Display an output.
        content = result.read()
        print(content)

    except Exception as e:
        print(f">>> Failed to get content from {url}")
        print(f">>> Error: {e}")


def main():
    url_content_printer()


if __name__ == "__main__":
    main()
