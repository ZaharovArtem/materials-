import json

class CatalogService:

    def __init__(self, path):
        self.path = path
        self.catalog = self.load_catalog()

    def load_catalog(self):
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def select_region(self):
        regions = {"1": "spb", "2": "msk", "3": "krd"}

        while True:
            print("\nВыберите регион:")
            print("1 - СПБ")
            print("2 - МСК")
            print("3 - КРД")

            choice = input("> ")

            if choice in regions:
                return regions[choice]
            else:
                print("Неверный ввод. Попробуйте снова.")

    def show_products(self, region):
        print("\nКаталог товаров:\n")

        for i, product in enumerate(self.catalog, start=1):
            price = product["prices"][region]
            print(f"{i}. {product['name']} — {price}")

    def choose_product(self):
        while True:
            try:
                choice = int(input("\nВыберите номер товара: "))
                if 1 <= choice <= len(self.catalog):
                    return self.catalog[choice - 1]
                else:
                    print("Такого товара нет.")
            except ValueError:
                print("Введите число.")