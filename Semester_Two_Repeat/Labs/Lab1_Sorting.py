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

# Bubble Sort function from Lecture Notes.
def bubbleSort(list):

    n = len(list)
    for i in range(n-1):
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

# Selection Sort function from Lecture Notes.
def selectionSort(myList):
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

# Insertion Sort function from Lecture Notes.
def insertionSort(list):
    n = len(list)
    i = 1
    while i < n:
        j = i-1
        while list[i] < list[j] and j > -1:
            j -= 1
        temp = list[i]
        k = i-1
        while k > j:
            list[k+1] = list[k]
            k -= 1
        list[k+1] = temp
        i += 1


#print("\nSelection Sort:")
#print(selection_sort(newList))

# Heap Sort Implementation
def heapSort(list):
    heapifyUp(list)

    length = len(list)
    for i in range(len(list)):
        list[0], list[length -1 -i] = list[length -1 -i], list[0]
        bubbleDown(list, 0, length-2-i)


# A Helper Method to turn a list into a heap
def heapifyUp(list):
    length = len(list)
    for i in range(length):
        bubbleUP(list, i)
  

# Bubble up the heap.
def bubbleUP(list, index):
    while index > 0:
        parent = (index-1) // 2
        if list[index] > list[parent]:
            list[index], list[parent] = list[parent], list[index]
            index = parent
        else:
            index = 0
    

# Bubble down the heap.
def bubbleDown(list, index, last):
    while last > (index*2):
        leftChild = index*2 + 1
        rightChild = index*2 + 2
        maxChild = leftChild
        if last > leftChild and list[rightChild] > list[leftChild]:
            maxChild = rightChild
        if list[index] < list[maxChild]:
            list[index], list[maxChild] = list[maxChild], list[index]
            index = maxChild
        else:
            index = last


## More efficient versions of HeapSort and Heapify
def heapSortBetter(list):
    heapifyDown(list)
    length = len(list)
    for i in range(length):
        list[0], list[length -1 -i] = list[length -1 -i], list[0]
        bubbleDown(list, 0, length-2-i)

def heapifyDown(list):
    length = len(list)
    for i in range((length-2)//2, -1, -1):
        bubbleDown(list, i, length-1)


## Testing
    
def testSorts():
    list1 = [7,3,9,4,1,8,10,5,2,6]
    heapifyUp(list1)
    print(list1, "Heapified (up) list")
    list2 = [7,3,9,4,1,8,10,5,2,6]
    heapifyDown(list2)
    print(list2, "Heapified (down) list")
    list5 = [7,3,9,4,1,8,10,5,2,6]
    heapSort(list5)
    print(list5, "heapsorted (up) list")
    list6 = [7,3,9,4,1,8,10,5,2,6]
    heapSortBetter(list6)
    print(list6, "heapsorted (down) list")
    list13 = [7,3,9,4,1,8,10,5,2,6]
    bubbleSort(list13)
    print(list13, "bubblesort list")
    list14 = [7,3,9,4,1,8,10,5,2,6]
    selectionSort(list14)
    print(list14, "selectionsort list")
    list15 = [7,3,9,4,1,8,10,5,2,6]
    insertionSort(list15)
    print(list15, "insertionsort list")

import random
import copy

def evaluateSorts():
    for i in range(4):  # so lists of size 10, 100, 1000, 10000 ... should see visible difference at 10000
        print("List size:", pow(10,i+1)) 
        list = [j for j in range(pow(10,i+1))]  # fill the list with integers from 0 up to list length-1
        random.shuffle(list)
        list2 = copy.copy(list)
        print("insertionsort starting ...")
        insertionSort(list)
        print("insertionsort finished")
        print("heapsort starting ...")
        heapSort(list2)
        print("heapsort finished")
        """ """        
        if i < 2:  # print the lists to check they have actually been sorted.
            print(list)
            print(list2)
        """ """

if __name__ == "__main__":
    testSorts()
    evaluateSorts()

