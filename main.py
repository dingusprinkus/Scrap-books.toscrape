from sql_analise import (
    search_per_category,
    avg_price_category_sql,
    price_higher_than,
    search_by_keyword,
)

while True:
    user_input = int(
        input(
            "\nSelecione uma opcao:\n"
            "1 - Mostrar Livros por Categoria\n"
            "2 - Ver preco Medio por Categoria\n"
            "3 - Mostrar Livros com um Preco Maior que o desejado\n"
            "4 - Procurar Livros que contenha uma palavra em especifico\n"
            "0 - Para Sair\n"
        )
    )

    if user_input == 1:
        book_search = search_per_category()

        for book_name in book_search:
            print(f"Nome do Livro: {book_name}\n")

    elif user_input == 2:
        avg_price = avg_price_category_sql()

        for name, price in avg_price:
            print(f"Categoria: {name}, Preco Medio: {price}")

    elif user_input == 3:
        select_price = price_higher_than(descending=True)

        for book_name, price in select_price:
            print(f"Nome Livro: {book_name}, Preco: {price}")

    elif user_input == 4:
        user_keyword = input("Digite uma Palavra:\n")
        search_keyword = search_by_keyword(user_keyword)

        for book_name, price in search_keyword:
            print(f"Nome Livro: {book_name}, Preco: {price}")

    elif user_input == 0:
        break

    else:
        print("Opcao Invalida\n")
        continue
