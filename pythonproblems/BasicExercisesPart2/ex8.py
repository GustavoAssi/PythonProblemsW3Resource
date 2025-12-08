from bs4 import BeautifulSoup
from urllib.request import urlopen


def google_news_top_stories() -> None:
    """
    This program retrieves the top stories from Google News.
    Author: Gustavo Assi Alencar.
    Date:   26/11/2025.
    """

    # Step 1: Set a url.
    news_url = "https://news.google.com/news/rss"

    # Step 2: Open url.
    client = urlopen(news_url)
    xml_page = client.read()
    client.close()

    # Step 3: Create a xml using Beautiful Soup.
    soup_page = BeautifulSoup(xml_page, "xml")

    # Step 4: Find all xml tags with news.
    news_list = soup_page.find_all("item")

    # Step 5: Display all news.
    for news in news_list:
        print(news.title.text)
        print(news.link.text)
        print(news.pubDate.text)
        print("-" * 60)


def main() -> None:
    google_news_top_stories()


if __name__ == "__main__":
    main()
