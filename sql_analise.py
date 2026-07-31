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

    cursor.execute(query)
    result = cursor.fetchall()
    conn.close

    return result
