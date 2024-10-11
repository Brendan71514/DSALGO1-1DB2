class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, e):
        self.items.append(e)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue on the empty queue")
        return self.items.pop(0)

    def first(self):
        if self.is_empty():
            raise IndexError("first from the empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

Q = Queue()

Q.enqueue(5)
Q.enqueue(3)
print(len(Q))
print(Q.dequeue())
print(Q.is_empty())
print(Q.dequeue())
print(Q.is_empty())
# print(Q.dequeue()) <-- IF I PUT THIS IN IT WILL RESULT IN AN ERROR
Q.enqueue(7)
Q.enqueue(9)
print(Q.first())
Q.enqueue(4)
print(len(Q))
print(Q.dequeue())
