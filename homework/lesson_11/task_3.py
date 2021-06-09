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

import pickle
from io import open
from typing import Dict
from product import Product
import json


class Store:
    nacenka: int
    store: Dict

    def __init__(self, name, nacenka):
        self.nacenka = nacenka
        self.name = name
        self.store = {}
        self.moneys = 0
        self.__filename = f"{self.name}.json"

    def add_product(self, prod: Product, count):
        self.store.update({prod: {"Count": count, "Sell_price": self.__calcprice(prod.price)}})

    def display(self):
        print(f"Store {self.name}. In cashbox  {self.moneys} money.")
        for prod, value in self.store.items():
            prod: Product
            value: Dict
            print(prod, value)

    def __calcprice(self, prod_price):
        return round(prod_price * (1 + self.nacenka / 100), 3)

    def __get_product(self, name):
        for prod in self.store:
            if prod.name == name:
                return prod
        return None

    def sell(self, prod_name, p_count):
        prod = self.__get_product(prod_name)
        if prod and self.store[prod]["Count"] >= p_count > 0:
            self.store[prod]["Count"] -= p_count
            self.moneys += self.store[prod]["Sell_price"] * p_count

    def save_pickle(self):
        with open(self.__filename, "wb") as fo:
            pickle.dump(self, fo)
        print("Store info successfully saved")

    def load_pickle(self):
        with open(self.__filename, 'rb') as fi:
            aself = pickle.load(fi)
            print("ALERT", aself.moneys)
        print("Store info successfully loaded")
        return aself

    def save_json(self):
        with open(self.__filename, "w") as fo:
            data = {"Moneys": self.moneys, "Store": []}
            slist = []
            for prod in self.store:
                adict = prod.get_dict()
                adict.update(self.store.get(prod))
                slist.append(adict)
            data["store"] = slist
            print(data)
            json.dump(data, fo)

    def load_json(self):
        with open(self.__filename) as fi:
            data = json.load(fi)
            self.moneys = data.pop("Moneys")
            self.store = {}
            for prods in data["Store"]:
                p = Product(prods.get("Name"), prods.get("Type"), prods.get("Price"))
                self.store[p] = {"Count": prods.get("Count"), "Sell_price": prods.get("sell_price")}
            print("Store info successfully loaded")

if __name__ == '__main__':
    a1 = Product("Хлеб", "Мучное", 10)
    a2 = Product("Булка", "Мучное", 12)
    a3 = Product("Батон", "Мучное", 14)

    s1 = Store("SuperStore", 15)
    s2 = Store("ASHOT", 85)

    s1.add_product(a1, 10)
    s1.add_product(a2, 10)
    s1.add_product(a3, 10)

    s2.add_product(a1, 5)
    s2.add_product(a2, 6)
    s2.add_product(a3, 4)

    # s1.display()
    # s2.display()

    s1.sell("Хлеб", 5)
    s2.sell("Хлеб", 2)
    s1.sell("Булка", 4)
    s2.sell("Булка", -10)
    # a1.name = 'Paneton'
    # a1.price = 305

    s1.display()
    # s2.display()
    s1.save_json()
    s1.store = {}
    s1.moneys = 0
    s1.display()
    s1.load_json()
    #
    # s1 = s1.load()
    s1.display()

