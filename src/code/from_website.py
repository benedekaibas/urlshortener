
import requests
from bs4 import BeautifulSoup



class SearchFromWebsite:
    """Class for scraping website."""
    def __init__(self) -> None:
        """Init function for the class."""
        pass

    def read_website(self):
        url = "https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/"
        scrape = requests.get(url)
        content = BeautifulSoup(scrape.content, 'html5lib')
        return content.prettify()
    
if __name__ == "__main__":
    search = SearchFromWebsite()
    website_content = search.read_website()
    print(website_content)