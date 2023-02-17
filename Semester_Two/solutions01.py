
""" Various sorting algorithms.

    Sample solutions for 1st lab, CS2516, 2022
"""


def insertionsort(mylist):
    """ Sort mylist using insertionsort, inserting from back.

    Args:
         mylist -- a python list to be sorted
    """

    #Assumes the sorted list implementation of the PQ

    #Convert the unsorted list into a PQ
    #for each index in turn, 
    #    ensure that all cells from 0 to that index are in sorted order
    #    (so for 0, nothing to do
    #        for 1, decide whether this item should go before or after the one currently in cell 0
    #        for 2, find the position in cells 0-1 to insert the current item, and shuffle up to make room
    #        for 3, find the position in cells 0-2 to insert the current item, and shuffle up to make room
    #        and so on)
 
    n = len(mylist)
    i = 1
    while i < n:
        j = i-1
        while mylist[i] < mylist[j] and j > -1:
            j -= 1
        #insert i in the cell after j
        temp = mylist[i]
        k = i-1
        while k > j:
            mylist[k+1] = mylist[k]
            k -= 1
        mylist[k+1] = temp
        i += 1
 



def heapsort(inlist):
    """ Sort a python list inplace, using heapsort.

    Args:
        inlist -- the python list to be sorted.
    """

    #Assumes the max binary heap implementation of the PQ, biggest item at root

    #Convert the unsorted list into a PQ
    length = len(inlist)
    for i in range(length):
        bubbleup(inlist,i)



    #Convert the PQ into a sorted list

    #for each index from the end working back to cell 0
    #ensure that the cells from index to the end contain the correct final slice of the final sorted list,
    #(so length-1 contains the biggest item, length-2 contains the 2nd biggest, and so on)
    #and the the cells from 0 up to index-1 maintan the other elements as a binary max heap, with the biggest remaining item in cell 0

    #so for cell length-1, we want the biggest item. It is currently stored in cell 0 at the root of the heap.
    #swap items in cell 0 and cell length-1. Now length-1 is no longer in the heap, but the item in cell 0 might be
    #breaking the heap property. so bubble down the item in cell 0, remembering that heap ends in cell length-2.
    #When that finishes, the biggest item in the heap is in cell 0, and that is the 2nd biggest item from the original list.
    #Now consider cell length-2. Swap item in cell 0 with the item in cell length-2. Shrink the view of the heap so that it ends in
    #cell length-3, and bubble down the item in cell 0.
    #And so on.  
    length = len(inlist)
    for i in range(length):
        inlist[0], inlist[length - 1 - i] = inlist[length - 1 - i], inlist[0]
        bubbledown(inlist,0, length-2-i)



def bubbleup(inlist, i):

    while i > 0:
        parent = (i-1) // 2
        if inlist[i] > inlist[parent]:
            # print('swapping:', inlist[i], 'with its parent:', inlist[parent])
            inlist[i], inlist[parent] = inlist[parent], inlist[i]
            i = parent
        else:
            i = 0


def bubbledown(inlist, i, last):

    while last > (i*2):  #so at least one child
        lc = i*2 + 1
        rc = i*2 + 2
        maxc = lc   # start by assuming left child is the max child
        if last > lc and inlist[rc] > inlist[lc]:  #rc exists and is bigger
            maxc = rc
        if inlist[i] < inlist[maxc]:
            # print('swapping:', inlist[i], 'with its child:', inlist[maxc])
            inlist[i], inlist[maxc] = inlist[maxc], inlist[i]
            i = maxc
        else:
            i = last



def testSorts():
    listforheap = [7,3,9,4,1,8,10,5,2,6]
    heapsort(listforheap)
    print(listforheap, "heapsorted list")
    listforins = [7,3,9,4,1,8,10,5,2,6]
    insertionsort(listforins)
    print(listforins, "insertionsort list")

import random
import copy

def evaluateSorts():
    for i in range(4):
        print("List size:", pow(10,i+1))
        list = [j for j in range(pow(10,i+1))]
        random.shuffle(list)
        list2 = copy.copy(list)
        print("insertionsort starting ...")
        insertionsort(list)
        print("insertionsort finished")
        print("heapsort starting ...")
        heapsort(list2)
        print("heapsort finished")
        """ """        
        if i < 2:  # print the lists to check they have actually been sorted.
            print(list)
            print(list2)
        """ """

if __name__ == "__main__":
    testSorts()
    evaluateSorts()

