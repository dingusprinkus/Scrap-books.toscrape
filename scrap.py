import csv

from bs4 import BeautifulSoup
import urllib.request
import re
import time

site = "https://books.toscrape.com/"

html_page = urllib.request.urlopen(site)

soup = BeautifulSoup(html_page, "html.parser")

books = []
category = []

# Encontra todas as <a> tags que contem category/books/ no href
for link in soup.find_all("a", href=lambda t: t and "category/books/" in t):
    href = link.get("href")
    
    # extrai apenas o texto das categorias
    name = link.text.strip()
    
    furl = site + href
    # print(furl)
    category.append((name, furl))


for name, cat_url in category:
    next_url = cat_url

    # Limitar num de pag pra teste
    page_count = 0
    max_page = 3

    while next_url and page_count < max_page:
        page = urllib.request.urlopen(next_url)
        soup = BeautifulSoup(page, "html.parser")

        for article in soup.find_all("article", class_=["product_pod", ""]):
            book_title = article.h3.a["title"]
            book_price = article.find("p", class_="price_color").get_text()
            convert_strip_price = float(book_price[1:])
            #print(book_title, name, book_price)
            books.append({"book": book_title, "category": name, "price": convert_strip_price})

        next_link = soup.find("li", class_="next")
        if next_link:
            next_href = next_link.a["href"]
            next_url = cat_url.rsplit("/", 1)[0] + "/" + next_href
        else:
            next_url = None

        page_count += 1


with open("scrap_books.csv", "w", encoding="utf-8") as file:
    write = csv.DictWriter(file, fieldnames=["book", "category", "price"])
    write.writeheader()
    write.writerows(books)
