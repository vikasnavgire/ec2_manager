import requests
from bs4 import BeautifulSoup
import json

# URL of the website to scrape
url = 'https://www.bbc.com/news'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the HTML elements containing the article titles and links
    articles = soup.find_all('div', class_='gs-c-promo')

    # Create a list to store the scraped data
    scraped_data = []

    # Loop through the articles and extract title and link
    for article in articles:
        title = article.find('h3', class_='gs-c-promo-heading__title').text
        link = article.find('a', class_='gs-c-promo-heading')['href']

        # Create a dictionary to store each article's data
        article_data = {
            'title': title,
            'link': link
        }

        scraped_data.append(article_data)

    # Save the scraped data to a JSON file
    with open('outputs/bbc_articles.json', 'w', encoding='utf-8') as json_file:
        json.dump(scraped_data, json_file, ensure_ascii=False, indent=4)

    print('Data scraped and saved to bbc_articles.json')
else:
    print('Failed to retrieve the webpage')

