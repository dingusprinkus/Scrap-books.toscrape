from sql_analise import search_per_category, avg_price_category_sql, price_higher_than

while True:
    user_input = int(
        input(
            "\nSelecione uma opcao:\n"
            "1 - Mostrar Livros por Categoria\n"
            "2 - Ver preco Medio por Categoria\n"
            "3 - Mostrar Livros com um Preco Maior que o desejado\n"
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
            print(f"Category: {name}, Average Price: {price}")

    elif user_input == 3:
        preco_input = int(input("Digite Preco: "))
        select_price = price_higher_than(preco_input, descending=True)

        for book_name, price in select_price:
            print(f"Book Name {book_name}, Price: {price}")

    elif user_input == 0:
        break

    else:
        print("Opcao Invalida\n")
        continue
