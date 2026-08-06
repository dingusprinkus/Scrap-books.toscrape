import sqlite3


def avg_price_category_sql(db_name="books.db", descending=False):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    order = "DESC" if descending else "ASC"

    query = f"""
            SELECT category, ROUND(AVG(price), 2) as avg_price 
            FROM books
            GROUP BY category
            ORDER BY avg_price {order}
            """

    print(query)
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()

    return result


def price_higher_than(price, db_name="books.db", descending=False):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    order = "DESC" if descending else "ASC"

    query = f"""
            SELECT book, price
            FROM books WHERE price > ?
            ORDER BY price {order}
            """

    cursor.execute(query, (price,))
    result = cursor.fetchall()
    conn.close()

    return result


def search_per_category(db_name="books.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT category FROM books")

    categories = [row[0] for row in cursor.fetchall()]

    for i, cat in enumerate(categories):
        print(f"{i} - {cat}")

    user_input = int(input("Escolha uma Categoria: "))
    user_choice = categories[user_input]

    query = "SELECT book FROM books WHERE category = ?"
    cursor.execute(query, (user_choice,))

    result = cursor.fetchall()
    conn.close()

    # for row in result:
    #     print(f"Book Name: {row[0]}")

    return result
