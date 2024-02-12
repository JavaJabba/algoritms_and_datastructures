'''
Lab 2: Quick Sort
'''
# Function to generate a list of integers of a given size.
from random import randint
def generateList(size):
    list = []
    i=0
    for i in range(size):
        newInt = randint(1, 99)
        list.append(newInt)
    return list

newList = generateList(10)
print("\nNew List:")
print(newList)

# Merge Sort Implementation
def mergeSort(myList):
    n = len(myList)
    if n > 1:
        list1 = myList[:n//2]
        list2 = myList[n//2:]
        mergeSort(list1)
        mergeSort(list2)
        merge(list1, list2, myList)
    return myList


def merge(list1, list2, myList):
    f1 = 0  #pointer1
    f2 = 0  #pointer2
    while f1 + f2 < len(myList):
        if f1 == len(list1):
            myList[f1+f2] = list2[f2]
            f2 += 1
        elif f2 == len(list2):
            myList[f1+f2] = list1[f1]
            f1 += 1
        elif list2[f2] < list1[f1]:
            myList[f1+f2] = list2[f2]
            f2 += 1
        else:
            myList[f1+f2] = list1[f1]
            f1 += 1     
    
#print(mergeSort(newList))


# Implementation of Quick Sort using Lomuto's Partitioning Scheme.

def quicksort(myList):
    n = len(myList)
    '''for i in range(len(myList)):
        j = randint(0, n-1)
        myList[i], myList[j] = myList[j], myList[i]'''
    _quicksort(myList, 0, n-1)

def _quicksort(myList, pointer, length):
    pivot = length
    print(pivot)
    earlyBig = 0
    while pointer < pivot:                                                          # While the check pointer hasn't reached the pivot.
        print("\nEarliest: "+ str(myList[earlyBig]))
        print("point: "+ str(myList[pointer]))
        print("pivot: "+ str(myList[pivot]))
        if myList[pointer] > myList[pivot]:
            pointer += 1
        elif myList[pointer] > myList[pivot] and earlyBig == 0:                     # Finding the earliest item thats bigger than the pivot.
            earlyBig = pointer                                                      # Setting the earlyBig.
            pointer += 1                                                            # Increment pointer by 1.
        elif myList[pointer] < myList[pivot]:                                       # If the value at the pointer is less than the pivot value.
            myList[pointer], myList[earlyBig] = myList[earlyBig], myList[pointer]   # Swap the values. 
            earlyBig += 1
            pointer += 1                                                            # increment both earlyBig and pointer.
            print("Swapped:")
            print(myList)
        else:
            pointer += 1
    myList[pivot], myList[earlyBig] = myList[earlyBig], myList[pivot]               # Once we reach the pivot swap it with earlyBig
    print("Break")
    _quicksort(myList, 0, earlyBig-1)
    _quicksort(myList, earlyBig+1, length)
    print("Sorted List:")
    print(myList)
         

quicksort(newList)