from handlers.joke_handler import get_joke
from handlers.product_handler import show_products, handle_product_query

def main():
    print("Привет! Я чат-бот. Вот что я умею:")
    print("1. Рассказать анекдот")
    print("2. Показать список товаров")
    print("3. Выйти")

    while True:
        choice = input("\nВыберите действие (1/2/3): ").strip()

        if choice == "1":
            print("\n" + get_joke())
        elif choice == "2":
            show_products()
            product_name = input("Введите название товара, чтобы узнать цену: ").strip()
            print(handle_product_query(product_name))
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неизвестная команда. Попробуйте ещё раз.")

if __name__ == "__main__":
    main()