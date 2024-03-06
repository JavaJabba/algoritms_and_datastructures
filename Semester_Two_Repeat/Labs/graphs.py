'''
Graphs
'''

class vertex:

    def __init__(self, element):
        self._element = element
        
    def __str__(self):
        str(self._element)
    
    def element(self):
        return str(self._element)


class edge:

    def __init__(self, x, y, element):
        self._vertices = (x, y)
        self._element = element
        
    def __str__(self):
        if self._firstVertex() == None:
            return "None"
        return ("(" + str(self._firstVertex()) + "--" + str(self._secondVertex()) + ":" + str(self._element))
    
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
    

class graph:

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
        v = vertex(element)
        self._keys[v] = dict()
        return v

    def add_edge(self, x, y, element):
        if not x in self._keys or not y in self._keys:
            return None
        e = edge(x, y, element)
        self._keys[x][y] = e
        self._keys[y][x] = e
        return e

    def remove_edge(e):
        pass

    def remove_vertex(x):
        pass


def test_graph():
    """ Test on a simple 3-vertex, 2-edge graph. """
    g = graph()
    a = g.add_vertex("a")
    b = g.add_vertex("b")
    c = g.add_vertex("c")
    eab = g.add_edge(a, b, 2)
    ebc = g.add_edge(b,c,9)

    vnone = vertex('dummy')
    evnone = g.add_edge(vnone, c, 0)   #should not create an edge
    if evnone is not None:
        print('ERROR: attempted edges  should have been none')

    edges = g.get_edges(vnone)     #should be None: vnone not in graph
    if edges != None:
        print('ERROR: returned edges for non-existent vertex.')
        
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

test_graph()