from ArrayStack_Act3_Docadoc import ArrayStack

def correct(expression):
    stack = ArrayStack()
    matching_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty() or stack.pop() != matching_pairs[char]:
                return False

    return stack.is_empty()

def reverse(file0):
    stack = ArrayStack()

    with open(file0, 'r') as file:
        for line in file:
            stack.push(line.rstrip('\n'))

    with open(file0, 'w') as file:
        while not stack.is_empty():
            file.write(stack.pop() + '\n')

def main():
    user_input = input("Enter an expression to see if it is balanced: ")
    result = correct(user_input)
    print(f"Expression: {user_input} is {'correct' if result else 'incorrect'}")

    file1 = 'file.txt'
    reverse(file1)
    print(f"The input per line in {file1} has been reversed.")

if __name__ == "__main__":
    main()