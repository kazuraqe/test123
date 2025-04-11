products = {
    "Кепка": 2000,
    "Худи": 4000,
    "Джинсовка": 5000,
    "Футболка": 2000
}
def show_products():
    print("\nСписок товаров")
    for name, price in products.items():
        print(f"-{name}")

def handle_product_query(product_name):
    if product_name in products:
        return f"Цена {product_name}: {products[product_name]} руб."
    else:
        return "Товар не найден."