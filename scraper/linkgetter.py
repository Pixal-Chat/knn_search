import requests
from bs4 import BeautifulSoup

# URL of the site you want to scrape
url = "https://techcrunch.com/category/artificial-intelligence/"

# Send a request to the website
response = requests.get(url)

# Parse the page content
soup = BeautifulSoup(response.content, "html.parser")

# Find the specific div or the entire page, depending on your needs
specific_div = soup.find('div', class_='wp-block-query is-layout-flow wp-block-query-is-layout-flow')  # Replace with your target div

# If the div is found, proceed with link extraction
if specific_div:
    links = specific_div.find_all('a', href=True)
    
    # Extract all links, excluding those containing "category" or "author"
    article_links = [
        link['href'] for link in links 
        if 'https://techcrunch.com/category' not in link['href'] and 
           'https://techcrunch.com/author' not in link['href']
    ]

    print("Filtered article links:", article_links)
else:
    print("The specified div was not found on the page.")

