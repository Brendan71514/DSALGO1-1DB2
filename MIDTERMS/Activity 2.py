class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, e):
        self.items.append(e)
        print(f"Enqueued: {e} (Queue: {self.items})")

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self.items.pop(0)
        print(f"Dequeued: {value} (Queue: {self.items})")
        return value

    def first(self):
        if self.is_empty():
            raise IndexError("first from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

if __name__ == "__main__":
    # Part 1
    print("\nPart 1")
    Q = Queue()

    Q.enqueue(5)
    Q.enqueue(3)
    print("Current length of queue:", len(Q))
    Q.dequeue()
    print("Is queue empty?", Q.is_empty())
    Q.dequeue()
    print("Is queue empty?", Q.is_empty())

    # print(Q.dequeue())  # if I try to type this. it will result in an error

    Q.enqueue(7)
    Q.enqueue(9)
    print("First element:", Q.first())
    Q.enqueue(4)
    print("Current length of queue:", len(Q))
    Q.dequeue()

    # Part 2
    print("\nPart 2")
    Q2 = Queue()
    Q2.enqueue(5)
    Q2.enqueue(3)
    print("Current length of queue:", len(Q2))
    Q2.dequeue()
    Q2.enqueue(2)
    Q2.enqueue(8)
    Q2.dequeue()
    Q2.dequeue()
    Q2.enqueue(9)
    Q2.enqueue(1)
    Q2.dequeue()
    Q2.enqueue(7)
    Q2.enqueue(6)
    Q2.dequeue()
    Q2.dequeue()
    Q2.enqueue(4)
    Q2.dequeue()
    Q2.dequeue()
