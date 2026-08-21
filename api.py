from fastapi import FastAPI
from sql_analise import avg_price_category_sql, price_higher_than

app = FastAPI()


@app.get("/preco-medio")
def get_avg_price(descending: bool = False):
    result = avg_price_category_sql(descending=descending)
    return result


@app.get("/livro/preco")
def get_price_higher_than(preco: float, descending: bool = False):
    result = price_higher_than(preco, descending=descending)
    return result
