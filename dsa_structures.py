
# 1. ARRAY
# Stores questions and accesses them by index.

class Array:
    def __init__(self):
        self.items = []

    def insert(self, value):
        self.items.append(value)

    def get(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]
        return None

    def size(self):
        return len(self.items)

    def display(self):
        return self.items


# 2. STACK
# Stores answer submission history (LIFO).

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# 3. QUEUE
# Processes questions in FIFO order.

class Queue:
    def __init__(self):
        self.items = []
        self.front = 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.is_empty():
            value = self.items[self.front]
            self.front += 1
            return value
        return None

    def is_empty(self):
        return self.front >= len(self.items)

    def size(self):
        return len(self.items) - self.front


# 4. NODE FOR CIRCULAR DOUBLY LINKED LIST

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# 5. CIRCULAR DOUBLY LINKED LIST
# Every node connects to the next and previous node.

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last = self.head.prev

            new_node.next = self.head
            new_node.prev = last

            last.next = new_node
            self.head.prev = new_node

        self.count += 1

    def get_node(self, index):
        if self.head is None or index < 0 or index >= self.count:
            return None

        current = self.head

        for _ in range(index):
            current = current.next

        return current

    def get(self, index):
        node = self.get_node(index)
        return node.data if node else None

    def next_node(self, node):
        return node.next if node else None

    def previous_node(self, node):
        return node.prev if node else None

    def display(self):
        values = []

        if self.head is None:
            return values

        current = self.head

        for _ in range(self.count):
            values.append(current.data)
            current = current.next

        return values

    def size(self):
        return self.count
