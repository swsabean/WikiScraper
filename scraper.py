import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the response
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the main content of the Wikipedia article
        main_content = soup.find(id='mw-content-text')

        # Extract the text from the main content
        text = main_content.get_text()

        return text
    else:
        # Return an error message if the request was not successful
        return f'Failed to scrape {url}. Error code: {response.status_code}'

if __name__ == '__main__':
    # Example URL for a Wikipedia article
    url = 'https://en.wikipedia.org/wiki/Web_scraping'

    # Scrape the text from the Wikipedia article
    text = scrape_wikipedia(url)

    # Print the extracted text
    print(text)
