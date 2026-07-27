from bs4 import BeautifulSoup
import urllib.request
import re

html_page = urllib.request.urlopen("https://books.toscrape.com")

soup = BeautifulSoup(html_page, "html.parser")

books = []
category = []

for link in soup.find_all("a", href=lambda t: t and "catalogue/" in t):
    href = link.get("href")
    split_parts = href.rstrip("/").split("/")
    # print(split_parts)

    slug = split_parts[-2] if split_parts[-1] == "index.html" else split_parts[-1]
    
    if "category/books/" in href:
        category.append(slug)
    elif href.startswith("catalogue/"):
        books.append(slug)


print("Books: \n", books)
print("Categories: \n", category)
