"""Task 3

Product Store

Write a class Product that has three attributes:

type
name
price
Then create a class ProductStore, which will have some Products and will operate with all products in the store.
All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement
additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your
store(30 percent)

set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by
input identifiers (type or name). The discount must be specified in percentage

sell_product(product_name, amount) - removes a particular amount of products from the store if available,
in other case raises an error. It also increments income if the sell_product method succeeds.

get_income() - returns amount of many earned by ProductStore instance.

get_all_products() - returns information about all available products in the store.

get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
```

class Product:

    pass

class ProductStore:

pass

p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product(Food, 'Ramen, 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell(‘Ramen’, 10)

assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)

```"""
from pprint import pprint


class Product:
    def __init__(self, type, name, price):
        self.price = price
        self.name = name
        self.type = type
        self.product_dict = {"Type": self.type, "Name": self.name, "Price": self.price}

    def __repr__(self):
        return f"{self.type}\t{self.name}"


class ProductStore:
        additional_price_percent: int

        def __init__(self, additional_price_percent):
            self.additional_price_percent = additional_price_percent
            self.store = {}

        def add(self, prod: Product, quantity):
            percent_from_price = prod.product_dict["Price"] / 100 * self.additional_price_percent
            new_price = prod.product_dict["Price"] + percent_from_price
            self.store.update({prod: {"Quantity": quantity, "Price": new_price}})

        def set_discount(self, prod: Product, identifier, percent, identifier_type=""):
            percent_from_price = prod.product_dict["Price"] * percent / 100
            print(percent_from_price)
            new_price = prod.product_dict["Price"] - percent_from_price
            print(new_price)
            for product in prod.product_dict:
                if identifier in prod.product_dict["Name"]:
                    prod.product_dict["Price"] = new_price

        def show_store(self):
            for prod, value in self.store.items():
                prod: Product
                value: dict
                print(prod, value)



p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product("Food", 'Ramen', 1.5)

s = ProductStore(30)
s.add(p, 30)
s.add(p2, 20)
s.set_discount(p, "Football T-Shirt", 10)
s.show_store()
# print(s.set_discount("Football T-short", 15))
# s.add(p, 10)




