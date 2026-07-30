def sort_by_price(df, descending=False):
    return df.sort_values("price", ascending=not descending)


def avg_price_category(df, descending=False):
    avg = df.groupby("category")["price"].mean().round(2)
    return avg.sort_values(ascending=not descending)
