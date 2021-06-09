import datetime
import random


class Inventory:
    koef = 1.0

    def __init__(self, price):
        self.price = price
        self.left_price = price

    def use_it(self):
        if not self.emergency_sit():
            self.left_price -= self.price * self.koef / 100
        else:
            self.left_price = 0
            print("ALARM! Device is dead!")

    def emergency_sit(self):
        return False

    def _select_zima_leto(self, summer, winter):
        cur_time = datetime.datetime.now()
        if 5 <= cur_time.month <= 10:
            return self.return_smth(summer)
        return self.return_smth(winter)

    def return_smth(self, posibility):
        return True if random.randint(1, 100) < posibility else False


class Sanki(Inventory):
    koef = 0.9

    def emergency_sit(self):
        return self._select_zima_leto(40, 3)


class Snowboard(Inventory):
    koef = 1.5

    def emergency_sit(self):
        cur_time = datetime.datetime.now()
        if cur_time.month in (1, 12):
            return self.return_smth(15)
        return self._select_zima_leto(50, 6)


class Luji(Inventory):
    koef = 1.3

    def emergency_sit(self):
        cur_time = datetime.datetime.now()
        if cur_time.day == 14 and cur_time.month == 2:
            return self.return_smth(90)


class Palki(Inventory):
    def emergency_sit(self):
        return self.return_smth(5)

def get_prihod():
    prihod_inv = []
    for i in range(1,100):
        cls = random.choice([Sanki, Snowboard, Luji, Palki])
        prihod_inv.append(cls(random.randint(100, 10000)))
    return prihod_inv