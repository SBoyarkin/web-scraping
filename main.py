from pprint import pprint
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
url = 'https://habr.com/ru/articles/'
base_url = 'https://habr.com/ru'
artile_list = []
result_list = []




KEYWORDS = ['дизайн', 'фото', 'web', 'python']

def check_world(words_lits, text):
    for word in words_lits:
        if word.lower() in text.lower():
            return True
        else: continue
    return False


def get_soup(url):
    response = requests.get(url)
    response_html = response.text
    soup = BeautifulSoup(response_html, 'lxml')
    return soup


article_tag = get_soup(url).find('div', class_='tm-articles-list')
article_tags = article_tag.find_all('article')

for article_tag in article_tags:
    pub_date = article_tag.find('time')['datetime']
    href = article_tag.find('a', class_='tm-article-datetime-published tm-article-datetime-published_link')['href']
    title = article_tag.find('h2', class_='tm-title tm-title_h2').text.strip()
    artile_list.append(
        {
            'pub_date': pub_date,
            'href': urljoin(base_url,href),
            'title': title,
        }
    )


# pprint(artile_list)

while len(artile_list) > 0:
    article = artile_list.pop()
    article_url = article.get('href')
    article_text = get_soup(article_url).find('div', class_='article-formatted-body')
    article_text = article_text.text
    check = check_world(KEYWORDS, article_text)
    if check:
        result_list.append(article)
    else:
        continue



print(len(result_list))





