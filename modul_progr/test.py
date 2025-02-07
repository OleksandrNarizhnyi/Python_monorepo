import requests
from bs4 import BeautifulSoup

html = requests.get('https://books.toscrape.com/', headers={"User-Agent": "Mozilla/5.0"}).text
soup = BeautifulSoup(html, "html.parser")


required_block = soup.find("ol", {"class": "row"})
all_books = required_block.find_all('li')


for book in all_books:
    book_name = book.find('h3').find('a')["title"]
    print(book_name)