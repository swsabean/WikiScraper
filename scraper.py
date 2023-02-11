import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the response
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the title of the article
        title = soup.find("h1", {"id": "firstHeading"}).get_text()

        return title
    else:
        # Return an error message if the request was not successful
        return f'Failed to scrape {url}. Error code: {response.status_code}'

if __name__ == '__main__':
    # Prompt the user for a Wikipedia page title
    page_title = input('Enter the title of a Wikipedia page: ')

    if page_title:
        # Build the URL for the Wikipedia article with the provided title
        url = f'https://en.wikipedia.org/wiki/{page_title}'
    else:
        # Choose a random Wikipedia page
        url = f'https://en.wikipedia.org/wiki/Special:Random'

    # Scrape the title from the Wikipedia article
    title = scrape_wikipedia(url)

    # Print the title
    print(f'Title: {title}')
    
