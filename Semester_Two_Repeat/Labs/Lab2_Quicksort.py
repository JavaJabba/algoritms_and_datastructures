'''
Lab 2: Quick Sort
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
    
print(mergeSort(newList))


# Implementation of Quick Sort using Lomuto's Partitioning Scheme.

def quicksort(myList):
    n = len(myList)
    for i in range(len(myList)):
        j = randint(0, n-1)
        myList[i], myList[j] = myList[j], myList[i]
    _quicksort(myList, 0, n-1)

def _quicksort(myList, point, length):
    pivot = myList[length]
    while point <= length:
        if point > pivot:
            greater = point
            point += 1
        
 
        