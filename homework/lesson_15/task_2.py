"""Task 2

Implement 2 classes, the first one is the Boss and the second one is the Worker.

Worker has a property 'boss', and its value must be an instance of Boss.

You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own
workers. You should implement a method that allows you to add workers to a Boss. You're not allowed to add instances
of Boss class to workers list directly via access to attribute, use getters and setters instead!

You can refactor the existing code.

```

id_ - is just a random unique integer



class Boss:

    def __init__(self, id_: int, name: str, company: str):

        self.id = id_

        self.name = name

        self.company = company

        self.workers = []



class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):

        self.id = id_

        self.name = name

        self.company = company

        self.boss = boss

```"""

# class Boss:
#
#     def __init__(self, id_: int, name: str, company: str):
#         self.id = id_
#         self.name = name
#         self.company = company
#         self.workers = []
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class Worker:
#
#     def __init__(self, id_: int, name: str, company: str, boss: Boss):
#         self.id = id_
#         self.name = name
#         self.company = company
#         self._boss = boss
#         boss.workers.append(Worker.__repr__(self))
#
#     def worker_info(self):
#         return f"Worker name is  {self.name}, he work at {self.company} and his boss is {self._boss}"
#
#     @property
#     def boss(self):
#         return self._boss
#
#     @boss.setter
#     def set_boss(self, boss: Boss):
#         self._boss = boss
#         boss.workers.append(Worker.__repr__(self))
#
#     @boss.deleter
#     def del_boss(self, boss):
#         print(f"Delete {self.boss} from {Worker.__repr__(self)}")
#         boss.workers.remove(Worker.__repr__(self))
#         del self._boss
#
#
#     def __repr__(self):
#         return f"{self.id}. {self.name}"

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []


    def __repr__(self):
        return f"{self.name}"



class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.__boss = boss
        self.id = id_
        self.name = name
        self.company = company

    @property
    def boss(self):
        return f"{self.__boss}"

    @boss.setter
    def boss(self, boss: Boss):
        self.__boss = boss
        boss.workers.append(self)

    def del_boss(self, boss: Boss):
        boss.workers.remove(self)

    def __repr__(self):
        return f"{self.id}. {self.name}"


if __name__ == '__main__':
    dante = Boss(18, "Vlad Fedyakin", "Apostera")
    dante1 = Boss(18, "Vlad Koltsov", "Dante Inc")
    vergil = Worker(11, "Bohdan Shulga", "Playrix", dante)
    vergil1 = Worker(12, "Bohdan Pidpalyi", "EA", dante)
    vergil.boss = dante
    vergil.del_boss(dante)
    vergil.boss = dante1
    print(f"Boss {dante} has {dante.workers}")
    print(f"Boss {dante1} has {dante1.workers}")
