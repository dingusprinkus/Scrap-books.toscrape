import csv
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
from analise import avg_price_category, sort_by_price
import sqlite3

site = "https://books.toscrape.com/"

html_page = urllib.request.urlopen(site)

soup = BeautifulSoup(html_page, "html.parser")

books = []
category = []

rating_system = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


# Encontra todas as <a> tags que contem category/books/ no href
for link in soup.find_all("a", href=lambda t: t and "category/books/" in t):
    href = link.get("href")

    # extrai apenas o texto das categorias
    name = link.text.strip()

    furl = site + href
    category.append((name, furl))


for name, cat_url in category:
    next_url = cat_url

    # Limitar num de pag pra teste
    page_count = 0
    max_page = 1

    while next_url and page_count < max_page:
        page = urllib.request.urlopen(next_url)
        soup = BeautifulSoup(page, "html.parser")

        for article in soup.find_all("article", class_="product_pod"):
            book_title = article.h3.a["title"]
            book_price = article.find("p", class_="price_color").get_text()
            book_rating = article.find("p", class_="star-rating")["class"]
            book_stock = article.find("p", class_="instock").get_text()

            convert_strip_price = float(book_price[1:])
            # Pega o ultimo index da lista do book_rating e mapeia a palavra para um numero usando a rating_system
            word_to_number_rating = rating_system[book_rating[-1]]

            in_stock = "In stock" in book_stock

            books.append(
                {
                    "book": book_title,
                    "category": name,
                    "price": convert_strip_price,
                    "star-rating": word_to_number_rating,
                    "in-stock": in_stock,
                }
            )

        next_link = soup.find("li", class_="next")
        if next_link:
            next_href = next_link.a["href"]
            next_url = cat_url.rsplit("/", 1)[0] + "/" + next_href
        else:
            next_url = None

        page_count += 1


def save_to_csv(books, filename="data_scrap_book.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        write = csv.DictWriter(
            file,
            fieldnames=[
                "book",
                "category",
                "price",
                "star-rating",
                "in-stock",
            ],
        )
        write.writeheader()
        write.writerows(books)


# df = pd.read_csv("data_scrap_book.csv")
# print(avg_price_category(df))
# print(sort_by_price(df))


def save_to_sql(books, db_name="books.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
                       CREATE TABLE IF NOT EXISTS books(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       book TEXT,
                       category TEXT,
                       price REAL,
                       rating INTEGER,
                       in_stock INTEGER
                       )
                        """)

    values = [
        (
            row["book"],
            row["category"],
            row["price"],
            row["star-rating"],
            row["in-stock"],
        )
        for row in books
    ]

    cursor.executemany(
        "INSERT INTO books (book, category, price, rating, in_stock) VALUES (?, ?, ?, ?, ?)",
        values,
    )

    conn.commit()
    conn.close()


save_to_sql(books)
