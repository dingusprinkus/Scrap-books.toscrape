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
    
        
    # split_parts = href.rstrip("/").split("/")
    # print(split_parts)

    # slug = split_parts[-2] if split_parts[-1] == "index.html" else split_parts[-1]

    # if "category/books/" in href:
    #     category.append(slug)
    # elif href.startswith("catalogue/"):
    #     books.append(slug)

for name, cat_url in category:
    next_url = cat_url
    
    # Limitar num de pag pra teste
    page_count = 0
    max_page = 3

    while next_url and page_count < max_page:
        page = urllib.request.urlopen(next_url)
        soup = BeautifulSoup(page, "html.parser")

        for article in soup.find_all("article", class_="product_prod"):
            book_tittle = article.h3.a["tittle"]
            print(book_tittle, name)
            #book.append({"book:" book_tittle, "category": name})
            
        next_link = soup.find("li", class_="next")
        if next_link:
            next_href = next_link.a["href"]
            next_url = cat_url.rsplit("/", 1)[0] + "/" + next_href
        else:
            next_url = None

        page_count += 1
        
            


# print("Books: \n", books)
print("Categories: \n", category)
