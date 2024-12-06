from LinkedStack import LinkedStack
from LinkedQueue import LinkedQueue

class Deque:
    """Double-ended queue implementation using a stack and a queue."""

    def __init__(self):
        """Create an empty deque."""
        self._stack = LinkedStack()
        self._queue = LinkedQueue()

    def is_empty(self):
        """Return True if the deque is empty."""
        return self._stack.is_empty() and self._queue.is_empty()

    def __len__(self):
        """Return the number of elements in the deque."""
        return len(self._stack) + len(self._queue)

    def add_first(self, e):
        """Add an element to the front of the deque."""
        self._stack.push(e)

    def add_last(self, e):
        """Add an element to the back of the deque."""
        self._queue.enqueue(e)

    def remove_first(self):
        """Remove and return the element at the front of the deque."""
        if self._stack.is_empty():
            if self._queue.is_empty():
                raise Exception('Deque is empty')
            while not self._queue.is_empty():
                self._stack.push(self._queue.dequeue())
        return self._stack.pop()

    def remove_last(self):
        """Remove and return the element at the back of the deque."""
        if self._queue.is_empty():
            if self._stack.is_empty():
                raise Exception('Deque is empty')
            while not self._stack.is_empty():
                self._queue.enqueue(self._stack.pop())
        return self._queue.dequeue()

    def first(self):
        """Return but do not remove the element at the front of the deque."""
        if self._stack.is_empty():
            if self._queue.is_empty():
                raise Exception('Deque is empty')
            while not self._queue.is_empty():
                self._stack.push(self._queue.dequeue())
        return self._stack.top()

    def last(self):
        """Return but do not remove the element at the back of the deque."""
        if self._queue.is_empty():
            if self._stack.is_empty():
                raise Exception('Deque is empty')
            while not self._stack.is_empty():
                self._queue.enqueue(self._stack.pop())
        return self._queue.first()

def test_deque():
    deque = Deque()

    print(deque.is_empty())
    print(len(deque))

    deque.add_first(10)
    deque.add_last(20)
    deque.add_first(5)
    deque.add_last(30)

    print("After adding elements:")
    print(deque.first())
    print(deque.last())
    print(len(deque))
    print(deque.remove_first())
    print(deque.remove_last())

    print("After removing elements:")
    print(deque.first())
    print(deque.last())
    print(len(deque))

    print(deque.remove_first())
    print(deque.remove_last())

    print(deque.is_empty())
    print(len(deque))
if __name__ == "__main__":
    test_deque()