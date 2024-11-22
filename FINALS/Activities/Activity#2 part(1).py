from LinkedStack import LinkedStack
import re
print("Arithmetic Equation to Postfix Expression")
infix_input = input("Enter an Equation: ")
stack = LinkedStack()
postfix = []
tokens = re.findall(r'\d+\.?\d*|[+\-*/()^]', infix_input)
for token in tokens:
    if token.replace('.', '').isdigit():
        postfix.append(token)
    elif token == '(':
        stack.push(token)
    elif token == ')':
        while not stack.is_empty() and stack.top() != '(':
            postfix.append(stack.pop())
        if not stack.is_empty() and stack.top() == '(':
            stack.pop()
    elif token in {'+', '-', '*', '/', '^'}:
        while (not stack.is_empty() and
               stack.top() != '(' and
               (token != '^' and (1 if stack.top() in {'+', '-'} else 2) >= (1 if token in {'+', '-'} else 2) or
                token == '^' and (3 if stack.top() == '^' else 2) > (3 if token == '^' else 2))):
            postfix.append(stack.pop())
        stack.push(token)
while not stack.is_empty():
    postfix.append(stack.pop())
postfix_expression = ' '.join(postfix)
print("\nPostfix Expression:", postfix_expression)