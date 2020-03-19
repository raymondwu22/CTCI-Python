from random import randint

class Node(object):
    # Function to initialize the node object
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNextNode(self):
        return self.next

    def setNextNode(self, data):
        self.next = data


class LinkedList(object):
    # Function to initialize head
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        self.size = 0
        if values:
            self.add_multiple(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x.data) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result


    def clear(self):
        trav = self.head
        while trav:
            next = trav.next
            trav.next = None
            trav.data = None
            trav = next
        self.head = trav = None
        self.size = 0

    def isEmpty(self):
        return len(self) == 0

    def add(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def add_to_beginning(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head

    def add_multiple(self, values):
        for v in values:
            self.add(v)

    def generate(self, n, min_value, max_value):
        self.head = self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self

class DoublyLinkedList(LinkedList):
    def add(self, value):
        if self.head is None:
            self.tail = self.head = Node(value, None, self.tail)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self