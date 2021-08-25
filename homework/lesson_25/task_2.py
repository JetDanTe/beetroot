"""Task 2

Implement a stack using a singly linked list."""
from node import Node

class Stack:

    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False


    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    def display(self):
        iternode = self.head
        if self.isempty():
            print("Stack Empty")
        else:
            while (iternode != None):
                print(iternode.data)
                iternode = iternode.next
            return


MyStack = Stack()

MyStack.push(18)
MyStack.push(11)
MyStack.push(20)
MyStack.display()
print("Fifo element is ", MyStack.peek())
MyStack.pop()
MyStack.pop()
MyStack.display()
print("Fifo element is ", MyStack.peek())

