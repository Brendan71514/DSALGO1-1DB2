
from LinkedDeque import LinkedDeque
from LinkedQueue import LinkedQueue

D = LinkedDeque()
D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(4)
D.insert_last(5)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)

Q = LinkedQueue()

Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
#Q[1 2 3 4]

D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
#D[5 6 7 8]
#D[5 6 7 8 1 2 3 4]
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_last())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
#Q[5 4 6 7 8]
#D[1 2 3]

D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
#D[1 2 3 5 4 6 7 8]

current = D._header._next
while current != D._trailer:
    print(current._element, end=' ')
    current = current._next