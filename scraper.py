
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

        # Find the first section header and its content
        first_header = main_content.find('h2')
        first_section = first_header.find_next_sibling('p')

        # Extract the text from the first section
        first_section_text = first_section.get_text()

        return text, first_header.get_text(), first_section_text
    else:
        # Return an error message if the request was not successful
        return f'Failed to scrape {url}. Error code: {response.status_code}'

if __name__ == '__main__':
    # Prompt the user for a Wikipedia page title
    page_title = input('Enter the title of a Wikipedia page: ')

    # Build the URL for the Wikipedia article
    url = f'https://en.wikipedia.org/wiki/{page_title}'

    # Scrape the text from the Wikipedia article
    text, first_header, first_section = scrape_wikipedia(url)

    # Print the extracted text, first section header, and first section content
    print(f'Text: {text}')
    print(f'First header: {first_header}')
    print(f'First section: {first_section}')
