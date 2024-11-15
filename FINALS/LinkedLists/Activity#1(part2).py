from LinkedDeque import LinkedDeque
from LinkedStack import LinkedStack

D = LinkedDeque()
D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(4)
D.insert_last(5)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)

S = LinkedStack()
S.push(D.delete_last())
S.push(D.delete_last())
S.push(D.delete_last())

D.insert_first(D.delete_last())
S.push(D.delete_last())
D.insert_last(D.delete_first())


D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())

current = D._header._next
while current != D._trailer:
    print(current._element, end=' ')
    current = current._next