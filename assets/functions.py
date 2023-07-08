import pandas as pd
import requests
from bs4 import BeautifulSoup as soup
from time import sleep
from tqdm import tqdm

# function to get url and beautify it
def get_url(url):
    r = requests.get(url)
    s = soup(r.content, 'html.parser')
    return s


# function to extract links, news, author and dates
def get_links_title(s):
    links = []
    news = []
    author =[]
    date =[]
    for u in s.find_all('div',class_='qt-item-header'):
        if 'NEWSLETTER' not in str(u):
            author.append(u.find('p', class_='qt-author').a.get_text(strip=True))
            date.append(u.find('p', class_='qt-date').get_text(strip=True))
            
            
    news_url  = s.find_all("div", class_="qt-header-bottom")
    titles =[title.get_text(strip=True) for title in s.find_all('h3',class_="qt-title") if 'NEWSLETTER' not in title.get_text(strip=True)]
    for new in news_url:
        extracted_links = [link['href'] for link in new.find_all('a', href=True) if 'author' not in link['href'] if 'newsletter' not in link['href']]
        if extracted_links:
            links.append(extracted_links[0])
            news_link = get_url(extracted_links[0])
            paragraphs = news_link.select_one('.qt-the-content').find_all('p')
            merged_text = ' '.join([p.get_text() for p in paragraphs])
            news.append(merged_text.strip())
            sleep(.05)
            
    return titles, news, links, date, author


# a repo-dictionary for tempral data storage
news_dict = {
    "title":[],
    'news':[],
    'links':[],
    'date':[],
    "author":[]
}

# function to convert the repo-dict to a pandas DataFrame
def create_csv(title, news, link, date, author):
    news_dict['title'].extend(title)
    news_dict['news'].extend(news)
    news_dict['links'].extend(link)
    news_dict['date'].extend(date)
    news_dict['author'].extend(author)
    
    return pd.DataFrame(news_dict)