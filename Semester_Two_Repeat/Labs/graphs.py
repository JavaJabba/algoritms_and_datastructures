'''
Graphs
'''

class Vertex:

    def __init__(self, element):
        self._element = element
        
    def __str__(self):
        str(self._element)
    
    def element(self):
        return str(self._element)


class Edge:

    def __init__(self, x, y, element):
        self._vertices = (x,y)
        self._element = element
        
    def __str__(self):
        return str(self._vertices), str(self._element)
    
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
            vertices += str(self._keys[v]) + " "
        edges = self.get_all_edges()
        edgestr = "\nEdges: "
        for e in edges:
            edgestr += str(e) + " "
        return vertices + edgestr
        
     
    def get_edge(self, x, y):
        if self._keys != None and x in self._keys and y in self._keys[x]:
            return self._keys[x][y]

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
        if not x in self._keys or not y in self._keys:
            return None
        e = Edge(x, y, element)
        self._keys[x][y] = e
        self._keys[y][x] = e
        return e

    def remove_edge(e):
        pass

    def remove_vertex(x):
        pass


# APQ Implementation for evaluating.
    
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
            strForm = "key: " + str(self._key) + " \tValue: " + str(self._value) + "\tIndex: " + str(self._index)
            return strForm

    def __init__(self):
        self._apq = []
        self._minElement = None

    def addItem(self, key, value):

        newElement = APQ.element(key, value, len(self._apq)-1)
        self._apq.append(newElement)

        if self.length() <= 1:
            self._minElement = newElement
        elif newElement.__lt__(self._minElement):
            self._minElement = newElement
        return self._apq
    
    def min(self):
        return self._minElement
    
    def removeMin(self):
        return
    
    def remove(self, element):
        if element[2] != self.length()-1:
            index = APQ.element.
            self._apq[index], self._apq[self.length()] = self._apq[self.length()], self._apq[index]
        element._wipe()

    def length(self):
        return len(self._apq)

    




def testadd():
    apq = APQ()
    a = apq.addItem(27, "Egg")
    b = apq.addItem(25, "sausage")
    print(apq.min())
    print(apq.remove(b))
    


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

testadd()