import requests
from bs4 import BeautifulSoup
import json  # <-- Import the json module
from datetime import datetime  # <-- (Optional) Import datetime for timestamp

url = 'https://mw.nyasatimes.com/category/news/'

# ... (the rest of the scraping code remains the same) ...

all_articles = []

for article in articles:
    title = article.h2.text if article.h2 else 'No title'
    link = article.find('a')['href']
    all_articles.append({
        'title': title,
        'link': link
    })
    print(f"Title: {title}\nLink: {link}\n")

# --- NEW FEATURE: Save to JSON File ---
# Generate a filename with a timestamp to avoid overwriting previous files
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f'chichewa_news_{timestamp}.json'

# Write the list of articles to the JSON file
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(all_articles, f, ensure_ascii=False, indent=4)

print(f"\n✅ Successfully saved {len(all_articles)} articles to {filename}")