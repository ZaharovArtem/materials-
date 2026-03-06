import json
from datetime import datetime


class OrderService:

    def show_order(self, product, region):
        price = product["prices"][region]

        print("\nВаш заказ:")
        print(f"Товар: {product['name']}")
        print(f"Категория: {product['category']}")
        print(f"Цена: {price}")

    def confirm(self):
        while True:
            answer = input("Оформляем заявку? (y/n): ").lower()
            if answer in ["y", "n"]:
                return answer
            print("Введите y или n")

    def find_cheapest_product(self, catalog, category, region):
        products = [p for p in catalog if p["category"] == category]
        return min(products, key=lambda p: p["prices"][region])

    def apply_discount(self, price):
        return round(price * 0.95, 2)

    def create_order(self, product, region, price):
        order = {
            "product": product["name"],
            "category": product["category"],
            "region": region,
            "price": price,
            "timestamp": datetime.now().isoformat()
        }

        try:
            with open("data/order.json", "r", encoding="utf-8") as f:
                orders = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            orders = []

        order["id"] = len(orders) + 1
        orders.append(order)

        with open("data/order.json", "w", encoding="utf-8") as f:
            json.dump(orders, f, ensure_ascii=False, indent=4)

        print(f"\nЗаявка №{order['id']} сохранена в order.json")

    def ask_new_order(self):
        while True:
            answer = input("\nСоздать новый заказ? (y/n): ").lower()
            if answer in ["y", "n"]:
                return answer
            print("Введите y или n")