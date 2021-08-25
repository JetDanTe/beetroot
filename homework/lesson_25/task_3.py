"""Task 3

Implement a queue using a singly linked list."""
from node import Node

class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def append(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def pop(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None

if __name__ == '__main__':
    q = Queue()
    q.append(1)
    q.append(2)
    q.append(3)
    q.pop()
    q.append(5)
    q.append(6)
    q.append(7)
    q.pop()
    print("Queue Front " + str(q.front.data))
    print("Queue Rear " + str(q.rear.data))