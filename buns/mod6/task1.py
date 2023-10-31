class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None

class LinkedList:
    def __init__(self):
        self.start = None

    def push(self, val):
        new_node = Node(val)
        if self.start is None:
            self.start = new_node
            return
        current = self.start
        while current.nref:
            current = current.nref
        current.nref = new_node

    def get(self, index):
        current = self.start
        count = 0
        while current and count < index - 1:
            current = current.nref
            count += 1
        return current.data

    def remove(self, index):
        if index < 0:
            return
        if index == 0:
            self.start = self.start.nref
            return
        current = self.start
        count = 0
        while current and count < index - 1:
            current = current.nref
            count += 1
        if current and current.nref:
            current.nref = current.nref.nref

    def insert(self, n, val):
        if n < 0:
            return
        new_node = Node(val)
        if n == 0:
            new_node.nref = self.start
            self.start = new_node
        else:
            current = self.start
            count = 0
            while current and count < n - 1:
                current = current.nref
                count += 1
            if current:
                new_node.nref = current.nref
                current.nref = new_node

    def __iter__(self):
        return LinkedListIterator(self.start)

class LinkedListIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.nref
            return data


