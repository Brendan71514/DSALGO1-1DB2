from LinkedStack import LinkedStack

class Deque:

    def __init__(self):
        """Create an empty deque."""
        self._left_stack = LinkedStack()
        self._right_stack = LinkedStack()

    def is_empty(self):
        """Return True if the deque is empty."""
        return self._left_stack.is_empty() and self._right_stack.is_empty()

    def __len__(self):
        """Return the number of elements in the deque."""
        return len(self._left_stack) + len(self._right_stack)

    def add_first(self, e):
        """Add an element to the front of the deque."""
        self._left_stack.push(e)

    def add_last(self, e):
        """Add an element to the back of the deque."""
        self._right_stack.push(e)

    def remove_first(self):
        """Remove and return the element at the front of the deque."""
        if self._left_stack.is_empty():
            while not self._right_stack.is_empty():
                self._left_stack.push(self._right_stack.pop())
        if self._left_stack.is_empty():
            raise Exception('Deque is empty')
        return self._left_stack.pop()

    def remove_last(self):
        """Remove and return the element at the back of the deque."""
        if self._right_stack.is_empty():
            while not self._left_stack.is_empty():
                self._right_stack.push(self._left_stack.pop())
        if self._right_stack.is_empty():
            raise Exception('Deque is empty')
        return self._right_stack.pop()

    def first(self):
        """Return but do not remove the element at the front of the deque."""
        if self._left_stack.is_empty():
            while not self._right_stack.is_empty():
                self._left_stack.push(self._right_stack.pop())
        if self._left_stack.is_empty():
            raise Exception('Deque is empty')
        return self._left_stack.top()

    def last(self):
        """Return but do not remove the element at the back of the deque."""
        if self._right_stack.is_empty():
            while not self._left_stack.is_empty():
                self._right_stack.push(self._left_stack.pop())
        if self._right_stack.is_empty():
            raise Exception('Deque is empty')
        return self._right_stack.top()

def test_deque():
    deque = Deque()
    print("Is deque empty?", deque.is_empty())
    print("Length of deque:", len(deque))
    deque.add_first(10)
    deque.add_last(20)
    deque.add_first(5)
    deque.add_last(30)
    print("After adding elements:")
    print("First element:", deque.first())
    print("Last element:", deque.last())
    print("Length of deque:", len(deque))

    print("Removed first element:", deque.remove_first())
    print("Removed last element:", deque.remove_last())

    print("After removing elements:")
    print("First element:", deque.first())
    print("Last element:", deque.last())
    print("Length of deque:", len(deque))

    # Remove remaining elements
    print("Removed first element:", deque.remove_first())
    print("Removed last element:", deque.remove_last())

    print("Is deque empty?", deque.is_empty())
    print("Length of deque:", len(deque))

if __name__ == "__main__":
    test_deque()