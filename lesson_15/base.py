import random

from lesson_15.inventory import Inventory


class Base:

    def __init__(self, name):
        self.name = name
        self.storage = []

    def add_asset_tag(self, inv_list):
        for i in inv_list:
            self.storage.append(Asset_tag(i, self))

    def give_inv(self, person):
        random.shuffle(self.storage)
        for i in self.storage:
            if i.user is None:
                i.user = person
                return i
        return None


class Asset_tag:

    def __init__(self, inv: Inventory, base: Base):
        self.base = base
        self.inv = inv
        self.user = None



