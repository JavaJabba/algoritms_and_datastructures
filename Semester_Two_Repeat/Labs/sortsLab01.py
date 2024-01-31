
""" Various sorting algorithms.

    Sample solutions for 1st lab, CS2516, 2024
"""


def bubblesort(mylist):
    """ Sort mylist inplace using basic bubblesort.

    Args:
         mylist -- a python list to be sorted
    """
    n = len(mylist)
    for i in range(n-1):
        for j in range(n-i-1):
            if mylist[j] > mylist[j+1]:
                mylist[j],mylist[j+1] = mylist[j+1], mylist[j]



""" High level abstract pseudocode for Priority Queue sorting

Convert the unsorted list into a PQ inplace, by taking each item in turn and
adding to the PQ, gradually expanding the virtual PQ each time
   (if the PQ is to be implemented as an unsorted list, nothing to do here)
Convert the PQ into a sorted list, by repeatedly taking the top ranked 
remaining item from the PQ and putting into the correct position, gradually
shrinking the PQ (and expanding the sorted list) each time
   (if the PQ is implemented as a sorted list, nothing to do here)
"""

def selectionsort(mylist):
    """ Sort mylist inplace using selectionsort.

    Args:
         mylist -- a python list to be sorted
    """
 
    #Assumes the unsorted list implementation of the PQ

    #Convert the unsorted list into a PQ
    #    (since we are using an unsorted list as the PQ, nothing to do here

    #Convert the PQ into a sorted list
    #for each index in turn, 
    #    ensure that all cells from 0 to that index contain the start of the sorted list
    #    (so for 0, find the smallest item in the list, and swap with what is in position 0;
    #        for 1, find the 2nd smallest item (which will be the smallest in cells 1 to end)
    #               and swap it with item in cell 1
    #        for 2, find the 3rd smallest item  (which will be smallest in cells 2 to end)
    #               and swap it with item in cell 2
    #        and so on

    n = len(mylist)
    i = 0
    while i < n:
        smallest = i
        j = i+1
        while j < n:
            if mylist[j] < mylist[smallest]:
                smallest = j
            j += 1
        mylist[i], mylist[smallest] = mylist[smallest], mylist[i]
        i += 1


def insertionsort(mylist):
    """ Sort mylist inplace using insertionsort, inserting from back.

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
    #        and so on
 
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
    #Convert the PQ into a sorted list
    #    (since the PQ we have built is a sorted list, nothing to do here)
 



def heapsort(inlist):
    """ Sort a python list inplace, using heapsort.

    Args:
        inlist -- the python list to be sorted.
    """

    #Assumes the max binary heap implementation of the PQ, biggest item at root

    #Convert the unsorted list into a PQ
    heapifyUp(inlist)

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


def heapifyUp(inlist):
    """ Turn a python list into a max binary heap, by bubbling up.

    Args:
        inlist - the python list to be sorted
    """

    #for each index in the list in turn, ensure cells from 0 to that index represent a max binary heap
    #so when we get to i in the iteration,  cells 0 to i-1 already contain a max binary heap, and we
    #effectively adding a new element (in cell i) into that heap. So we juse use the standard procedure
    #and bubble that item up the heap.

    length = len(inlist)
    for i in range(length):
        bubbleup(inlist,i)


def heapsortbetter(inlist):
    """ Sort a python list inplace, using heapsort, with a more efficient heapify.

    Args:
        inlist -- the python list to be sorted.
    """

    heapifyDown(inlist)
    length = len(inlist)
    for i in range(length):
        # no change from other version
        inlist[0], inlist[length - 1 - i] = inlist[length - 1 - i], inlist[0]
        bubbledown(inlist,0, length-2-i)


#A more efficient function to turn an unsorted list into a heap, used in heapsortbetter(...)
#See Lab01 Q4 for an explanation of the iteration.
def heapifyDown(inlist):
    """ Turn a python list into a max binary heap, by bubbling down.

    Args:
        inlist - the python list to be sorted
    """
    length = len(inlist)
    for i in range((length-2)//2, -1, -1):
        bubbledown(inlist, i, length-1)


def bubbleup(inlist, i):
    """ Bubble up an item in pos i in a max heap to its final position.

    Args:
        inlist -- a python list of a max heap, in transition
        i -- index of the item that may need to be bubbled up the heap
    """
    while i > 0:
        parent = (i-1) // 2
        if inlist[i] > inlist[parent]:
            # print('swapping:', inlist[i], 'with its parent:', inlist[parent])
            inlist[i], inlist[parent] = inlist[parent], inlist[i]
            i = parent
        else:
            i = 0


def bubbledown(inlist, i, last):
    """ Bubble down an item in pos i in a max heap to its final position.

    Note that the parameter 'last' was not needed in the version from Semester 1
    but we need it here since the heap ends before the end of inlist, and so we
    must not bubbledown beyond that last item.

    Args:
        inlist -- a python list of a max heap, in transition
        i -- index of the item that may need to be bubbled down
        last - index of the last item in the current max heap
    """
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
    list1 = [7,3,9,4,1,8,10,5,2,6]
    heapifyUp(list1)
    print(list1, "Heapified (up) list")
    list2 = [7,3,9,4,1,8,10,5,2,6]
    heapifyDown(list2)
    print(list2, "Heapified (down) list")
    list5 = [7,3,9,4,1,8,10,5,2,6]
    heapsort(list5)
    print(list5, "heapsorted (up) list")
    list6 = [7,3,9,4,1,8,10,5,2,6]
    heapsortbetter(list6)
    print(list6, "heapsorted (down) list")
    list13 = [7,3,9,4,1,8,10,5,2,6]
    bubblesort(list13)
    print(list13, "bubblesort list")
    list14 = [7,3,9,4,1,8,10,5,2,6]
    selectionsort(list14)
    print(list14, "selectionsort list")
    list15 = [7,3,9,4,1,8,10,5,2,6]
    insertionsort(list15)
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

