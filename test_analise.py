import pandas as pd

from analise import avg_price_category, sort_by_price


def test_short_by_price():
    df = pd.DataFrame({"price": [40, 192, 2, 120939]})
    result = sort_by_price(df, descending=False)
    assert list(result["price"] == [40, 192, 2, 120939])


def test_avg_price_category():
    df = pd.DataFrame(
        {
            "category": [
                "Fiction",
                "Fiction",
                "Horror",
                "Horror",
                "Fantasy",
                "Fantasy",
            ],
            "price": [10, 24, 40, 11, 55, 99],
        }
    )
    result = avg_price_category(df, descending=False)
    assert result["Fiction"] == 17
    assert result["Horror"] == 25.5
    assert result["Fantasy"] == 77
