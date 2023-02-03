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
        self.item = (key, value)
        self._heap.append(self.item)
        self._parentNode = self._heap[(self.item-1)/2]
        self._rightChild = self._heap[(self.item*2)+2]
        self._leftChild = self._heap[(self.item*2)+1]
        
        if self._heap[self.item] > self._heap[parentNode]:
            tempVal =self._parentNode
            self._parent

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