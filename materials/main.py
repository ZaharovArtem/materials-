from service.catalog_service import CatalogService
from service.order_service import OrderService


class App:

    def __init__(self):
        self.catalog_service = CatalogService("data/catalog.json")
        self.order_service = OrderService()

    def run(self):

        while True:

            print("\n" + "=" * 40)

            region = self.catalog_service.select_region()

            self.catalog_service.show_products(region)

            product = self.catalog_service.choose_product()

            self.order_service.show_order(product, region)

            answer = self.order_service.confirm()

            price = product["prices"][region]

            if answer == "y":
                self.order_service.create_order(product, region, price)

            else:

                cheapest = self.order_service.find_cheapest_product(
                    self.catalog_service.catalog,
                    product["category"],
                    region
                )

                if cheapest["name"] != product["name"]:

                    print("\nМы можем предложить более дешевый вариант:")

                    new_price = cheapest["prices"][region]

                    print(f"{cheapest['name']} — {new_price}")

                    if self.order_service.confirm() == "y":
                        self.order_service.create_order(
                            cheapest,
                            region,
                            new_price
                        )

                else:

                    discount_price = self.order_service.apply_discount(price)

                    print(f"Предлагаем скидку 5%: {discount_price}")

                    if self.order_service.confirm() == "y":
                        self.order_service.create_order(
                            product,
                            region,
                            discount_price
                        )

            if self.order_service.ask_new_order() == "n":
                print("\nСпасибо за использование приложения!")
                break


if __name__ == "__main__":
    app = App()
    app.run()