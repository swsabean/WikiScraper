
import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the response
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the author of the article
        author = soup.find("a", {"class": "fn"})
        if author:
            author = author.get_text()
        else:
            author = "Author not found"

        return author
    else:
        # Return an error message if the request was not successful
        return f'Failed to scrape {url}. Error code: {response.status_code}'

if __name__ == '__main__':
    # Prompt the user for a Wikipedia page title
    page_title = input('Enter the title of a Wikipedia page: ')

    # Build the URL for the Wikipedia article
    url = f'https://en.wikipedia.org/wiki/{page_title}'

    # Scrape the text from the Wikipedia article
    author = scrape_wikipedia(url)

    # Print the extracted text, first section header, and first section content
    print(f'Author:{author}')
