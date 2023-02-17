'''
Student Name: Dylan Murray
Student Number: 121747725

Algorithms and Data Structures II 
Assignment 1: Comparison of Sorting Algorithms

All work was carried out using lab and lecture notes.
A Max heap was in progress for implementation but I was unable to complete in time 
therefore is commented out and I used a prepared heap array for testing.
I also ran out of time to implement the second half of the quick sort.
'''
import time, random


# Max Heap
'''
class BinaryHeap:


    class Element:
  

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __greater__(self, other):
            return self._key > other._key

        def __wipe__(self):
            self._key = None
            self._value = None

    def __init__(self):
        self._heap = []
        self._size = 0

    def add(self, key, value):
        add (key,value) to the heap 
        self.item = (key, value)
        self._heap.append(self.item)

        if self._heap[len(self._heap)-1] > self._parent(len(self._heap)-1):
            self._upHeap()


    def max(self):
        return self._heap[0]

    def remove_max(self):
        self._heap.remove[0]
        
        find next max number by checking left or right.
        then bubble sort down.
        

    def length(self):
        return self._size

    # private methods

    def _left(self, index):
        left = self._heap[(2*index)+1]
        return left

    def _right(self, index):
        right = self._heap[(2*index)+2]
        return right

    def _parent(self, index):
        pos = (index -1) % 2
        parent = self._heap[pos]
        return parent

    def _upHeap(self):
        #bubble sort up list
        n = len(self._heap)
        for i in range(n-1):
            for j in range(0,n-i-1):
                parent = self._parent(j)
                if self._heap[j] > self._parent(j):
                    self._heap[j], parent = parent, self._heap[j]

    def _downHeap(self):
        #bubble sort down list
        
        #keep bubbling down until reach the end of array signifying next empty space
        
        n = len(self._heap)
        for i in range(n-1):
            for j in range(n-i-1, 0):
                parent = self._parent(j)
                if self._heap[j] > self._parent(j):
                    self._heap[j], parent = parent, self._heap[j]


    def _testadd():
        print('Testing that we can add items to an array-based binary heap PQ')
        pq = BinaryHeap()
        print('pq has size:', pq.length(), '(should be 0)')
        pq.add(25,'25')
        pq.add(4, '4')
        print('pq has size:', pq.length(), '(should be 2)')
        print(pq, '(should be 4,25, could also show index and value)')
        pq.add(19,'19')
        pq.add(12,'12')
        print(pq, '(should be 4,12,19,25)')
        pq.add(17,'17')
        pq.add(8,'8')
        print(pq, '(should be 4,12,8,25,17,19)')
        print('pq length:', pq.length(), '(should be 6)')
        print('pq max item:', pq.max(), '(should be 4)')
        print()
        print(pq._heap)
        return pq

BinaryHeap._testadd()'''

# Heap Sort

def heapsort(inlist):

    length = len(inlist)
    for i in range(length):
        bubbleup(inlist,i)
    
    length = len(inlist)
    for i in range(length):
        inlist[0], inlist[length - 1 - i] = inlist[length - 1 - i], inlist[0]
        bubbledown(inlist,0, length-2-i)
    return inlist

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

    while last > (i*2):  
        lc = i*2 + 1
        rc = i*2 + 2
        maxc = lc  
        if last > lc and inlist[rc] > inlist[lc]:  
            maxc = rc
        if inlist[i] < inlist[maxc]:
            # print('swapping:', inlist[i], 'with its child:', inlist[maxc])
            inlist[i], inlist[maxc] = inlist[maxc], inlist[i]
            i = maxc
        else:
            i = last
# used to test heap sort
# testlist = [4,12,8,25,17,19]
# print(heapsort(testlist))



# Merge Sort
def mergesort(mylist):
    n = len(mylist)
    if n > 1:
        list1 = mylist[:n//2]
        list2 = mylist[n//2:]
        mergesort(list1)
        mergesort(list2)
        merge(list1, list2, mylist)
    return mylist

def merge(list1, list2, mylist):
    f1 = 0
    f2 = 0
    while f1 + f2 < len(mylist):
        if f1 == len(list1):
            mylist[f1+f2] = list2[f2]
            f2 += 1
        elif f2 == len(list2):
            mylist[f1+f2] = list1[f1]
            f1 += 1
        elif list2[f2] < list1[f1]:
            mylist[f1+f2] = list2[f2]
            f2 += 1
        else:
            mylist[f1+f2] = list1[f1]
            f1 += 1

# Quick Sort
def quicksort(mylist):
    n = len(mylist)
    for i in range(len(mylist)):
        print(mylist)
        j = random.randint(0, n-1)
        mylist[i], mylist[j] = mylist[j], mylist[i]
    
    # sort(mylist, 0, n-1)
'''
pseudocode sort(list, pivot, end)
    while searches not crossed
        search to right from pivot for a bigger item     
        search to left from end for a smaller item
        if searches not crossed
            swap items
    swap pivot with most recently found small item
    sort(list, small, pivot)
    sort(list, pivot+1, end)'''

# def sort(list, pivot, end):

# testlist = [4,12,8,25,17,19]

# quicksort(testlist)

# Insertion Sort
def insertion_sort(mylist):
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
    return mylist


# The Testing Zone!

def checksorted(list:list, func):
    '''
    Check sorted list method  
    '''
    func = func.__name__
    i = 0
    for i in range(len(list)-1):
        if list[i] < list[i+1]:
            i+1
        else:
            return func + " is not sorted!"
    return "List Sorted!"

def testonealg(inlist, f):
    start_time = time.perf_counter()
    f(inlist)
    end_time = time.perf_counter()
    checksorted(inlist, f)
    return end_time - start_time

def randomlist(n, k):
    mylist = []
    i = 0
    for i in range(0, n):
        newint = random.randint(1, 99)
        for j in range(0, k):
            mylist.append(newint)
        i + 1
    random.shuffle(mylist)
    return mylist

# testlist = randomlist(6,2)
# print(testonealg(testlist, insertion_sort))

def evaluate(n, k, num, f):
    masterlist = []
    times = []
    i = 0
    j = 0
    for i in range(0, num):
        newlist = randomlist(n, k)
        masterlist.append(newlist)
        i+1 
    for j in range(len(masterlist)-1):
        currentlist = masterlist[j]
        runtime = testonealg(currentlist, f)
        times.append(runtime)
    avg = float(sum(times) / (len(times)-1))
    return "\n" + f.__name__ + " ran for: \t" + str(avg) + " seconds on average!\n"

# print(evaluate(10, 2, 10, insertion_sort))

def evaluate_all(n, k, nums, funcs):
    masterlist = []
    i = 0
    print("Functions are tested with lists of size " + str(n) + " with " + str(k) + " duplicates!")
    for i in range(0, nums):
        newlist = randomlist(n, k)
        masterlist.append(newlist)
        i+1 

    f = 0
    for f in range(len(funcs)):
        l = 0
        times = []
        for l in range(len(masterlist)-1):
            currentlist = masterlist[l]
            runtime = testonealg(currentlist, funcs[f])
            times.append(runtime)
            l + 1
        avg = float(sum(times) / (len(times)-1))
        print("\n" + funcs[f].__name__ + " ran for: \t\t\t" + str(avg) + " seconds on average!")
        f + 1

funcs = [insertion_sort, heapsort, mergesort]
print(evaluate_all(6, 2, 10, funcs))

def evaluate_scale():
    parameters = [(100, 20),
                  (1000, 200),
                  (10000, 2000),
                  (100000, 20000)]
    functions = [mergesort, heapsort, insertion_sort]
    for (n, k) in parameters:
        evaluate_all(n, k, 20, functions)

# print(evaluate_scale())

def evaluate_all_partial(n, k, d, num, funcs):
    masterlist = []
    i = 0
    print("Functions are tested with partially sorted lists of size " + str(n) + " with " + str(k) + " duplicates!")
    for i in range(0, num):
        newlist = randomlist(n, k)
        newlist = insertion_sort(newlist)
        swaps = n//d
        s = 0
        for s in range(0, swaps):
            j = random.randint(0, n-1)
            newlist[s], newlist[j] = newlist[j], newlist[s]
            s + 1
        masterlist.append(newlist)
        i+1 

    f = 0
    for f in range(len(funcs)):
        l = 0
        times = []
        for l in range(len(masterlist)-1):
            currentlist = masterlist[l]
            runtime = testonealg(currentlist, funcs[f])
            times.append(runtime)
            l + 1
        avg = float(sum(times) / (len(times)-1))
        print("\n" + funcs[f].__name__ + " ran for: \t\t\t" + str(avg) + " seconds on average!")
        f + 1
        
print(evaluate_all_partial(6, 2, 2, 10, funcs))