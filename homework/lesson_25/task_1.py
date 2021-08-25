"""Task 1
Extend UnorderedList

Implement append, index, pop, insert methods for UnorderedList. Also implement a slice method, which will take two
parameters `start` and `stop`, and return a copy of the list starting at the position and going up to but not including
the stop position."""

from node import Node


class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def append(self, item):
        if self.head == None:
            self.head = Node(item)
        else:
            newnode = Node(item)
            newnode.next = self.head
            self.head = newnode

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def index(self, item):
        pass

    def pop(self, item):
        current = self.head
        previous = None
        found = False
        while not found:

            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())










