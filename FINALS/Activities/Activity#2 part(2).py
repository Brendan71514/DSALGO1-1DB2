from PositionalList import PositionalList as PositionalList
P = PositionalList()
numbers = [1, 72, 81, 25, 65, 91, 11]
for number in numbers:
    P.add_last(number)
print("Original PositionalList elements:")
for x in P:
    print(x)
if P.first() is not None:
    marker = P.first()
    while marker != P.last():
        pivot = P.after(marker)
        value = pivot.element()
        if value > marker.element():
            marker = pivot
        else:
            walk = marker
            while walk != P.first() and P.before(walk).element() > value:
                walk = P.before(walk)
            P.delete(pivot)
            P.add_before(walk, value)
    print("\nSorted in Ascending Order:")
    for x in P:
        print(x)
if P.first() is not None:
    marker = P.first()
    while marker != P.last():
        pivot = P.after(marker)
        value = pivot.element()
        if value < marker.element():
            marker = pivot
        else:
            walk = marker
            while walk != P.first() and P.before(walk).element() < value:
                walk = P.before(walk)
            P.delete(pivot)
            P.add_before(walk, value)
    print("\nSorted in Descending Order:")
    for x in P:
        print(x)