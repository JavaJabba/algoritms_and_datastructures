'''
Student Name: Dylan Murray
Student Number: 121747725

Algoritms and Data Structures II: Lab One: Binary Heap Queue
'''
import time

class BinaryHeap:
    '''
    '''

    class Element:
        '''
        '''

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
        ''' add (key,value) to the heap '''
        self.item = (key, value)
        self._heap.append(self.item)
        self._parentNode = self._heap[(self.item-1)/2]
        self._rightChild = self._heap[(self.item*2)+2]
        self._leftChild = self._heap[(self.item*2)+1]
        
        if self._heap[self.item] > self._heap[parentNode]:
            tempVal =self._parentNode
            self._parent

    def max(self):
        return self._heap[0]

    def remove_max(self):
        self._heap.remove[0]
        #bubble sort down from top


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
        parent = self._heap[(index-1)/2]
        return parent

    def _upHeap(self):
        #bubble sort up list
        n = len(self._heap)
        for i in range(n-1):
            for j in range(0,n-i-1):
                if self._heap[j] > self._heap[j+1]:
                    self._heap[j], self._heap[j+1] = self._heap[j+1], self._heap[j]
        pass

    def _downHeap(self):
        #bubble sort down list
        pass

<<<<<<< Updated upstream

    def _testadd():
        # print('Testing that we can add items to an array-based binary heap PQ')
        pq = BinaryHeap()
        # print('pq has size:', pq.length(), '(should be 0)')
        pq.add(25,'25')
        pq.add(4, '4')
        # print('pq has size:', pq.length(), '(should be 2)')
        # print(pq, '(should be 4,25, could also show index and value)')
        pq.add(19,'19')
        # pq.add(12,'12')
        # print(pq, '(should be 4,12,19,25)')
        # pq.add(17,'17')
        # pq.add(8,'8')
        # print(pq, '(should be 4,12,8,25,17,19)')
        # print('pq length:', pq.length(), '(should be 6)')
        # print('pq max item:', pq.max(), '(should be 4)')
        # print()
        print(pq._heap)
        return pq

BinaryHeap._testadd()
=======
def checksorted(list:list):

    i = 0
    for i in range(len(list-1)):
        if list[i] > list[i+1]:
            i+1
        else:
            return "List Unsorted"


def testonealg(inlist, f):
    start_time = time.perf_counter()
    f(inlist)
    end_time = time.perf_counter()
    checksorted(inlist, f)
    return end_time - start_time

>>>>>>> Stashed changes
