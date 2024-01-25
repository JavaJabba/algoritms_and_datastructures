'''
Lab 1: Sorting Algorithms.
Goal: Evaluate Sorting algorithms; Selection Sort, Heap Sort
'''

# Function to generate a list of integers of a given size.
from random import randint
def generateList(size):
    list = []
    i=1
    for i in range(1, size):
        newInt = randint(1, 99)
        list.append(newInt)
    return list

newList = generateList(10)
print("\nNew List:")
print(newList)

# Selection Sort function from Lecture Notes.
def selection_sort(myList):
    n = len(myList)
    i = 0
    while i < n:
        smallest = i
        j = i+1
        while j < n:
            if myList[j] < myList[smallest]:
                smallest = j
            j += 1
        myList[i], myList[smallest] = myList[smallest], myList[i]
        i += 1
    return myList

#print("\nSelection Sort:")
#print(selection_sort(newList))

# Heap Sort Implementation
def heapSort(newList):
    heap = newList[0:2]
    i = 2
    while i <= len(newList-1):
        parent = (i-1)//2
        if heap[i] > heap[parent]:
            bubbleUP(heap, i)
        i += 1
        heap.append(newList[i])
    #phase 2
    i = len(heap-1)
    while i > 1:
        #swap
        tempVal = heap[0]
        heap[0] = heap[i]
        heap[i] = tempVal
        #bubble top item
        top = heap[0]
        right = (2*i) + 1
        left = (2*i) + 2
        if right >= left:
            largest = right
            bubbleDown(heap, i, )
        elif left >= right:
            largest = left
        i -= 1


    






    

# Helper method to bubble up the heap.
def bubbleUP(list, index):
    return

# Helper method to bubble down the heap.
def bubbleDown():
    return