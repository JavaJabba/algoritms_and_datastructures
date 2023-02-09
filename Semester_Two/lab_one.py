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
        pass

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
