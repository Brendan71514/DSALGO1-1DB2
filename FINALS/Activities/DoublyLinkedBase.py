class _DoublyLinkedBase:
    """A base class for a doubly linked list."""

    class _Node:
        """A lightweight, non-public class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)  # sentinel node at the front
        self._trailer = self._Node(None, self._header, None)  # sentinel node at the back
        self._header._next = self._trailer  # header is linked to trailer
        self._size = 0  # number of elements in the list

    def is_empty(self):
        """Return True if the list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two nodes and return the new node."""
        new_node = self._Node(e, predecessor, successor)
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node):
        """Remove a node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None  # clear the node
        return element