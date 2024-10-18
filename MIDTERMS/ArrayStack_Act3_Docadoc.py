class ArrayStack:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data.pop()


if __name__ == "__main__":
    stack = ArrayStack()
    stack.push(1)
    stack.push(2)
    print("Top element:", stack.top())
    print("Stack size:", len(stack))
    print("Popped element:", stack.pop())
    print("Stack is empty:", stack.is_empty())