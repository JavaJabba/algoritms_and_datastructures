#rename this file to PQBinaryHeap.py

class PQBinaryHeap:
    """ Maintain an collection of items, popping by lowest key.

        This implementation maintains the collection using a binary heap.
        Uses an internally-defined class Element to store the items as a
        key (i.e. priority) and value (i.e. the actual item) pair.
        Use this class by typing PQBinaryHeap.Element() etc.
    """
    class Element:
        """ An element with a key and value. """
        
        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            """ Return True if this key equals the other key. """
            return self._key == other._key

        def __lt__(self, other):
            """ Return True if this key is less than the other key. """
            return self._key < other._key

        def _wipe(self):
            """ Set the instance variables to None. """
            self._key = None
            self._value = None

    def __init__(self):
        """ Create a PQ with no elements. """

        # this is an array-based heap, so you need to create
        # an empty python list, and then maintain it
        # properly in the add and remove-min methods.
        self._heap = []
        self._size = 0
        
    def __str__(self):
        """ Return a breadth-first string of the values. """
        # method body goes here

    #
    # First, the four standard methods for the ADT

    def add(self, key, value):
        """ Add Element(key,value) to the heap. """
        # method body goes here

    def min(self):
        """ Return the min priority key,value. """
        # method body goes here

    def remove_min(self):
        """ Remove and return the min priority key,value. """
        # method body goes here

    def length(self):
        """ Return the number of items in the heap. """
        # method body goes here

    #
    # Now, the methods needed for the underlying heap implementation
    # These are designated 'private', with the leading underscore, since
    # client code should not have access to these - all access to the PQ
    # is meant to be via the standard 4 methods
    # You don't need to implement these if they are
    # not used in your 4 standard methods above, but
    # I find them useful.

    def _left(self, posn):
        """ Return the index of the left child of elt at index posn. """
        # method body goes here

    def _right(self, posn):
        """ Return the index of the right child of elt at index posn. """
        # method body goes here

    def _parent(self, posn):
        """ Return the index of the parent of elt at index posn. """
        # method body goes here

    def _upheap(self, posn):
        """ Bubble the item in posn in the heap up to its correct place. """
        # method body goes here

    def _downheap(self, posn):
        """ Bubble the item in posn in the heap down to its correct place. """
        # method body goes here

    def _printstructure(self):
        """ Print out the elements one to a line. """
        for elt in self._heap:
            if elt is not None:
                print('(', elt._key, ',', elt._value, ')')
            else:
                print('*')

    def _testadd():
        print('Testing that we can add items to an array-based binary heap PQ')
        pq = PQBinaryHeap()
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
        print('pq min item:', pq.min(), '(should be 4)')
        print()
        return pq

    def _test():
        print('Testing that we can add and remove items from an array-based binary heap PQ')
        pq = PQBinaryHeap()
        print('pq has size:', pq.length())
        loc = {}
        print('Adding ant with value 25')
        loc['ant'] = pq.add(25,'ant')
        print('pq has size:', pq.length())
        print(pq)
        print('Adding bed with value 4')
        loc['bed'] = pq.add(4, 'bed')
        print(pq)
        print('Adding cat with value 14')
        loc['cat'] = pq.add(14,'cat')
        print(pq)
        print('Adding dog with value 12')
        loc['dog'] = pq.add(12,'dog')
        print(pq)
        print('Removing first')
        min = pq.remove_min()
        print("Just removed", str(min))
        print(pq)
        print('Adding egg with value 17')
        loc['egg'] = pq.add(17,'egg')
        print(pq)
        print('Adding fox with value 8')
        loc['fox'] = pq.add(8,'fox')
        print(pq)
        print('pq length:', pq.length())
        print('pq min item:', pq.min())
        for i in range(pq.length()):
            key, value = pq.remove_min()
            print('removed min (', key, value, '):', pq)

PQBinaryHeap._testadd()
PQBinaryHeap._test()
