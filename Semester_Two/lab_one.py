'''
Student Name: Dylan Murray
Student Number: 121747725

Algoritms and Data Structures II: Lab One: Binary Heap Queue
'''

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
        ''' return max value (top of heap) '''
        pass

    def remove_max(self):
        ''' remove max value then resort '''
        pass        

    def length(self):
        return self._size

    # private methods

    def _left(self):
        pass

    def _right(self):
        pass

    def _parent(self):
        pass

    def _upHeap(self):
        pass

    def _downHeap(self):
        pass
