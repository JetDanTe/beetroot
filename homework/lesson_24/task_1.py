"""Task 1

Write a program that reads in a sequence of characters and prints them in reverse order, using your
implementation of Stack."""

class Stack:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def __repr__(self):
        representation = "Reversed input:\n"
        for item in reversed(self._items):
            representation += f"{str(item)}"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    stack_1 = Stack()
    input_str = input("Enter some charachetes:\n")
    for i in input_str:
        stack_1.add(i)
    print(stack_1)
