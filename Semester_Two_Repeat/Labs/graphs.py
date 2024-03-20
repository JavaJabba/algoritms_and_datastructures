'''
Graphs
'''
from random import randint

# Graph Implementation

class Vertex:

    def __init__(self, element):
        self._element = element
        
    def __str__(self):
        return " {} ".format(self._element)
    
    def element(self):
        return self._element


class Edge:

    def __init__(self, x, y, element):
        self._vertices = (x,y)
        self._element = element
        
    def __str__(self):
        return "{} -- {} : {} ".format(self._vertices[0], self._vertices[1], self._element)
    
    def __repr__(self):
        return str(self)
    
    def vertices(self):
        return self._vertices

    def opposite(self, x):
        if self._vertices[0] == x:
            return self._vertices[1]
        elif self._vertices[1] == x:
            return self._vertices[0]
        else:
            return None
        
    def element(self):
        return self._element
    
    def _firstVertex(self):
        return self._vertices[0]

    def _secondVertex(self):
        return self._vertices[1]
    

class Graph:

    def __init__(self):
        self._keys = dict()

    def __str__(self):
        vertices = "Vertices: "
        for v in self._keys:
            vertices += str(v) + " "
        edges = self.get_all_edges()
        edgestr = "\nEdges: "
        for e in edges:
            edgestr += str(e) + " "
        return vertices + edgestr
    
    def __repr__(self):
        return str(self)
    
    def get_edge(self, x, y):
        if self._keys != None and x in self._keys and y in self._keys[x]:
            return self._keys[x][y]
        return None

    def degree(self, x):
        return len(self._keys[x])

    def get_all_edges(self):
        edgelist = []
        for x in self._keys:
            for y in self._keys[x]:
                if self._keys[x][y]._firstVertex() == x:
                    edgelist.append(self._keys[x][y])
        return edgelist

    def get_edges(self, x):
        if x in self._keys:
            edgeList = []
            for y in self._keys[x]:
                edgeList.append(self._keys[x][y])
            return edgeList
        return None
    
    def vertices(self):
        return [key for key in self._keys]

    def num_vertices(self):
        return len(self._keys)

    def num_edges(self):
        num = 0
        for v in self._keys:
            num += len(self._keys[v])
        return num//2

    def add_vertex(self, element):
        v = Vertex(element)
        self._keys[v] = dict()
        return v

    def add_edge(self, x, y, element):
        if x not in self._keys or y not in self._keys:
            return None
        e = Edge(x, y, element)
        self._keys[x][y] = e
        self._keys[y][x] = e
        return e

    def remove_edge(e):
        pass

    def remove_vertex(x):
        pass

# APQ Unsorted List Implementation for evaluating.
    
class APQ:


    class element:
        
        def __init__(self, key, value, index):
            self._key = key           
            self._value = value
            self._index = index

        def __eq__(self, other):
            return self._key == other._key
        
        def __lt__(self, other):
            return self._key < other._key
        
        def _wipe(self):
            self._key = None
            self._value = None
            self._index = None

        def __str__(self):
            strForm = "key: " + str(self._key) + " \tValue: " + str(self._value[0]._element) + "\tIndex: " + str(self._index)
            return strForm

    def __init__(self):
        self._apq = []
        self._minElement = ()

    def __str__(self):
        strForm = ""
        for i in self._apq:
            strForm += "( "+ str(i) +" ) \n"
        return strForm

    def __repr__(self):
        return str(self)
    
    def addItem(self, key, value):
        index = len(self._apq)
        newElement = APQ.element(key, value, index)
        self._apq.append(newElement)

        if self.length() == 1:
            self._minElement = self._apq[0]
        elif newElement.__lt__(self._minElement):
            self._minElement = newElement
        return (key, value, index)
    
    def min(self):
        return self._minElement
    
    def removeMin(self):
        self.remove(self._minElement)
        minEle = self._apq[randint(0, self.length()-1)]
        for ele in self._apq:
            if ele._value[0]._element < minEle._value[0]._element:
                minEle = ele
        self._minElement = minEle
        return minEle._value[0]
    
    def remove(self, element):
        if element._index != self.length()-1:
            index = element._index
            self._apq[index], self._apq[self.length()-1] = self._apq[self.length()-1], self._apq[index]
            self.updateIndex(index, index)
        return self._apq.pop()

    def length(self):
        return len(self._apq)
    
    def updateIndex(self, index, newIndex):
        ele = self._apq[index]
        ele._index = newIndex
    
# APQ Heap implementation for evaluating.
        
class APQHeap:

    class element:
        
        def __init__(self, key, value, index):
            self._key = key           
            self._value = value
            self._index = index

        def __eq__(self, other):
            return self._key == other._key
        
        def __lt__(self, other):
            return self._key < other._key
        
        def _wipe(self):
            self._key = None
            self._value = None
            self._index = None

        def __str__(self):
            strForm = "key: " + str(self._key) + " \tValue: " + str(self._value) + "\tIndex: " + str(self._index)
            return strForm

    def __init__(self):
        self._apq = []

    def __str__(self):
        strForm = ""
        for i in self._apq:
            strForm += "( "+ str(i) +" ) "
        return strForm

    def __repr__(self):
        return str(self)
    
    def addItem(self, key, value):
        index = len(self._apq)
        newElement = APQHeap.element(key, value, index)
        self._apq.append(newElement)
        
        parent = self._apq[index % 2]
        if parent._key > key:
            index = self.bubbleUP(self._apq, index)
        return (key, value, index)

    def bubbleUP(self, list, index):
        while index > 0:
            parent = (index-1) / 2
            if list[index] > list[parent]:
                list[index], list[parent] = list[parent], list[index]
                index = parent
        return index
    
    def min(self):
        return self._apq[0]

    def removeMin(self):
        self._apq[0], self._apq[self.length()-1] = self._apq[self.length()-1], self._apq[0]
        self._apq.pop()
        self.bubbleDown(self._apq, 0, len(self._apq)-1)
        return self.min()

    def length(self):
        return len(self._apq)

    def bubbleDown(self, list, index, last):
        while last > (index*2):
            leftChild = index*2 + 1
            rightChild = index*2 + 2
            maxChild = leftChild
            if last > leftChild and list[rightChild] > list[leftChild]:
                maxChild = rightChild
            if list[index] < list[maxChild]:
                list[index], list[maxChild] = list[maxChild], list[index]
                index = maxChild

    def remove(self, element):
        if element[2] != self.length()-1:
            index = element[2]
            self._apq[index], self._apq[self.length()-1] = self._apq[self.length()-1], self._apq[index]
        self._apq.pop()
        return self._apq[self.length()-1]

# Random Graph Generator.
def buildRandomGraph(n, m):
    g = Graph()
    vertices = []
    i = 0
    for i in range(0, n):
        ref = g.add_vertex(str(i))
        vertices.append(ref)
        weight = randint(1, 20)
        if i >= 2:
            index = vertices[randint(0, len(vertices)-1)]
            last = vertices[-1]
            if str(index) == str(last):
                index = vertices[randint(0, len(vertices)-1)]
            g.add_edge(index, last, weight)
        i += 1
    j = 0
    for j in range(m, (n-1)):
        weight = randint(1, 20)
        x = vertices[randint(0, len(vertices)-1)]
        y = vertices[randint(0, len(vertices)-1)]
        if str(x) == str(y):
            y = vertices[randint(0, len(vertices)-1)]
        if g.get_edge(x, y) == None and g.get_edge(y, x) == None:
            e = g.add_edge(x, y, weight)
        j += 1
    print("\nGraph Created:\n" + str(g))
    return g


#buildRandomGraph(10, 8)
# Prims Algorithm
    
def primList():
    # Build graph and initialise APQ and locs Dictionary.
    G = buildRandomGraph(10, 8)
    apq = APQ()
    locs = dict()
    mst = []
    index = 0
    # Populate apq and locs dict for each vertex in graph.
    for v in G.vertices():
        apq.addItem(float('inf'), (v, None))
        locs[v] = index
        index += 1
    i = 0
    print(apq)
    while apq:
        print("iter: " + str(i))
        i+=1
        minEle = apq.removeMin()
        print("removed " + str(minEle))
        print(str(apq) + "\n")
        del locs[minEle]
        cost = 0
        minCost = 0
        edgelist = G.get_edges(minEle)
        print(edgelist)
        if edgelist != None:
            for edge in edgelist:
                if edge not in mst:
                    if len(edgelist) == 1:
                        mst.append(edge)
                    if edge._secondVertex() in locs:
                        if cost == 0:
                            print("1")
                            cost = edge._element
                        if cost > edge._element:
                            print("2")
                            cost = edge._element
                            minCost = edge
                if minCost != 0:
                    mst.append(minCost)
        print(mst)
    return mst
            
        
print(primList())

def primHeap():
    # Build graph and initialise APQ and locs Dictionary.
    G = buildRandomGraph(10, 5)
    apq = APQHeap()
    locs = dict()
    mst = []
    index = 0
    for v in G.vertices():
        apq.addItem(float('inf'), (v, None))
        locs[v] = index
        index += 1
    while apq:
        min = apq.removeMin()
        locs.pop()

def testadd():
    apq = APQHeap()
    a = apq.addItem(27, "Egg")
    b = apq.addItem(25, "sausage")
    print(apq)
    apq.removeMin()
    print(apq)

#testadd()

def test_graph():
    """ Test on a simple 3-vertex, 2-edge graph. """
    g = Graph()
    a = g.add_vertex("a")
    b = g.add_vertex("b")
    c = g.add_vertex("c")
    eab = g.add_edge(a,b,2)
    ebc = g.add_edge(b,c,9)
    
    print('number of vertices:', g.num_vertices())
    print('number of edges:', g.num_edges())

    print("Degree of a should be 1\n")
    g.degree(a)

    print('Vertex list should be a,b,c in any order :')
    vertices = g.vertices()
    for key in vertices:
        print(key.element())

    print('Edge list should be (a,b,2),(b,c,9) in any order :')
    edges = g.get_all_edges()
    for edge in edges:
        print(edge)

    print('Graph display should repeat the above:')
    print(g)

    v = g.add_vertex('d')
    edges = g.get_edges(v)
    if edges != []:
        print('ERROR: should have returned an empty list, but got', edges)
    print('Graph should now have a new vertex d with no edges')
    print(g)

