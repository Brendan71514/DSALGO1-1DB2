'''
def InsertionSort(arr1):
    for i in range(1, len(arr1)):
        key = arr1[i]

        j = i - 1
        # move lement of arr1(0..i-1)
        # that are greater than the key
        # to one position ahead of
        # their current position
        while j >= 0 and key < arr1[j]:
            arr1[j + 1] = arr1[j]
            j -= 1
        arr1[j + 1] = key
arr1 = [10, 2, 3, 1, 1, 4, 89, 21]
print("arr1 before insertion sort")
print(arr1)
InsertionSort(arr1)
#print values array 1
print("arr1 after insertion sort")
print(arr1)



#SELECTION SORT

def SelectionSort(arr2):
    for i in range(len(arr2)):
        min_idx = i
        for j in range(i + 1, len(arr2)):
            if arr2[min_idx] > arr2[j]:
                min_idx = j
            # SWAPPING THE VALUES OF ARRAY
        arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]
arr2 = [10, 2, 3, 1, 1, 4, 89, 21]
print("array 2 before selection sort")
print(arr2)
SelectionSort(arr2)
print("arr 2 values after selection sort")
print(arr2)



#BUBBLE SORT
def BubbleSort(arr3):
    for i in range(len(arr3)):
        for j in range(0, len(arr3) - i - 1):
            if arr3[j] > arr3[j + 1]:
                arr3[j], arr3[j + 1] = arr3[j + 1], arr3[j]
arr3 = [10, 2, 3, 1, 1, 4, 89, 21]
print("array 3 before bubble sort")
print(arr3)
BubbleSort(arr3)
print("arr 3 values after bubble sort")
print(arr3)
'''

#1
def BubbleSortAscending(arr1):
    for i in range(len(ar1)):
        for j in range(0, len(ar1) - i - 1):
            if ar1[j] > ar1[j + 1]:
                ar1[j], ar1[j + 1] = ar1[j + 1], ar1[j]

ar1 = [23,89, 7, 56, 44]
print("Number 1 before bubble sort")
print(ar1)
BubbleSortAscending(ar1)
print("Number 1 values after bubble sort")
print(ar1)
print()
#2
def InsertionSortAscending(arr1):
    for i in range(1, len(arr1)):
        key = arr1[i]
        j = i - 1
        while j >= 0 and key < arr1[j]:
            arr1[j + 1] = arr1[j]
            j -= 1
        arr1[j + 1] = key
num2 = [12, 78, 91, 34, 62]
print("Number 2 before insertion sort")
print(num2)
InsertionSortAscending(num2)
#print values array 1
print("Number 2 after insertion sort")
print(num2)
print()
#3
def SelectionSortDescending(arr2):
    for i in range(len(arr2)):
        min_idx = i
        for j in range(i + 1, len(arr2)):
            if arr2[min_idx] < arr2[j]:
                min_idx = j
            # SWAPPING THE VALUES OF ARRAY
        arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]
num3 = [5, 99, 48, 15, 67]
print("Number 3 before selection sort")
print(num3)
SelectionSortDescending(num3)
print("Number 3 values after selection sort")
print(num3)
print()
#4
def InsertionSortDescending(arr1):
    for i in range(1, len(arr1)):
        key = arr1[i]
        j = i - 1
        while j >= 0 and key > arr1[j]:
            arr1[j + 1] = arr1[j]
            j -= 1
        arr1[j + 1] = key
num4 = [38, 82, 25, 74, 13]
print("Number 4 before insertion sort")
print(num4)
InsertionSortDescending(num4)
#print values array 1
print("Number 4 after insertion sort")
print(num4)
print()

#5
num5 = [44, 56, 62, 78, 48, 15, 38, 74]
print("Number 5 Before Sorting")
print(num5)
InsertionSortAscending(num5)
print("Number 5 after Ascending sort")
print(num5)
InsertionSortDescending(num5)
print("Number 5 after Descending sort")
print(num5)
print()

#6
def SelectionSortAscending(arr2):
    for i in range(len(arr2)):
        min_idx = i
        for j in range(i + 1, len(arr2)):
            if arr2[min_idx] > arr2[j]:
                min_idx = j
        arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]
num6 = [23,89, 7, 56, 44, 12, 78, 91, 34, 62, 5, 99, 48, 15, 67, 38, 82, 25, 74, 13]
print("Number 6 before selection sort")
print(num6)
SelectionSortDescending(num6)
print("Number 6 values after selection Ascending sort")
print(num6)
print()

#7
def evenNum(arr):
    even= []
    for num in arr:
        if num % 2 == 0:
            even.append(num)
    return even
def oddNum(arr):
    odd = []
    for num in arr:
        if num % 2 != 0:
            odd.append(num)
    return odd
print("Number 7 before odd even sort")
print(num6)
even = evenNum(num6)
odd = oddNum(num6)
print("Even numbers:")
print(even)
print("Odd numbers:")
print(odd)
