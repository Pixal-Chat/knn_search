import requests
from bs4 import BeautifulSoup
import pymongo 
import urllib 
from datetime import datetime

# MongoDB setup (replace these with your MongoDB connection details)
client = pymongo.MongoClient("MONGO_DB_URL")  # Replace with your MongoDB URI
db = client["data"]  # Database name
collection = db["elastic_data"]  # Collection name

# URL of the site you want to scrape
url = "https://techcrunch.com/2024/10/11/instagram-blames-moderation-issues-on-human-reviewers-not-ai/"

# Send a request to the website
response = requests.get(url)

# Parse the page content
soup = BeautifulSoup(response.content, "html.parser")

# Initialize data dictionary to store scraped data
news_data = {}

# Find the specific div by its class that contains an h1 tag
specific_div = soup.find('div', class_='article-hero__middle')

# Check if the div with the specific class and h1 tag is found
if specific_div and specific_div.find('h1'):
    # Extract the <h1> content
    h1_text = specific_div.find('h1').get_text().strip()
    news_data["title"] = h1_text
    print(f"Title (h1): {h1_text}")
else:
    print("The specified div with an h1 tag was not found or the h1 tag is missing.")

# Find the specific div containing the author information (with class 'wp-block-tc23-author-card-name')
author_div = soup.find('div', class_='wp-block-tc23-author-card-name')

# Check if the div with the author name is found
if author_div and author_div.find('a'):
    # Extract the text inside the <a> tag (author name)
    author_name = author_div.find('a').get_text().strip()
    news_data["author"] = author_name
    print(f"Author Name: {author_name}")
else:
    print("The specified div with an author name was not found or the <a> tag is missing.")

# Find the specific div with class "entry-content wp-block-post-content is-layout-constrained wp-block-post-content-is-layout-constrained"
content_div = soup.find('div', class_='entry-content wp-block-post-content is-layout-constrained wp-block-post-content-is-layout-constrained')

# Check if the div is found
if content_div:
    # Extract text from all <p> tags inside this div
    paragraph_texts = [p.get_text().replace('\xa0', ' ').strip() for p in content_div.find_all('p')]

    # Extract text from all nested <div> tags inside this div
    nested_div_texts = [div.get_text().replace('\xa0', ' ').strip() for div in content_div.find_all('div')]

    # Combine the content from <p> and nested <div> tags
    all_content = paragraph_texts + nested_div_texts
    news_data["content"] = " ".join(all_content)  # Join all content into one string

    print("Content inside the specific div with multiple <p> and <div> tags:")
    print(paragraph_texts)
else:
    print("The specified content div was not found.")

# Find the specific div containing an img tag (replace with the correct class)
img_div = soup.find('div', class_='article-hero__first-section')

# Check if the div with the img tag is found
if img_div and img_div.find('img'):
    # Extract the src attribute from the img tag
    img_src = img_div.find('img')['src']
    news_data["image_src"] = img_src
    print(f"Image Source: {img_src}")
else:
    print("The specified div with an img tag was not found or the img tag is missing.")

# Insert the data into MongoDB
collection.insert_one(news_data)
print("Data successfully inserted into MongoDB!")
