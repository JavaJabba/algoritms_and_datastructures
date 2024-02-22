'''
Graphs
'''

class vertex():

    def __init__(self, element):
        self._element = element
        
    def __str__(self):
        str(self._element)


class edge():

    def __init__(self, x, y, element):
        self._vertices = (x, y)
        self._element = element
        
    def __str__(self):
       return (str(self._vertices[0]) + "--" + str(self._vertices[1]))

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
    
    def _firstVertex(self, x):
        return x

    def _secondVertex(self, y):
        return y
    

class graph():

    def __init__(self):
        self._keys = dict()

    def get_edge(self, x, y):
        if self._keys != None and x in self._keys and y in self._keys[x]:
            return self._keys[x][y]

    def degree(self, x):
        return len(self._keys[x])

    def get_edges(self, x):
        edgeList = []
        if x in self._keys:
            for y in self._keys[x]:
                edgeList.append(self._keys[x][y])
            return edgeList
        return None

    def add_vertex(self, element):
        v = vertex(element)
        self._keys[v] = dict()
        return v

    def add_edge(self, x, y, element):
        if x not in self._keys or y not in self._keys:
            return None
        e = edge(x, y, element)
        self._keys[x][y] = e
        self._keys[y][x] = e
        return e

    def remove_edge(e):
        pass

    def remove_vertex(x):
        pass


graphtest = graph()
graphtest.add_vertex("x")
graphtest.add_vertex("y")
graphtest.add_edge("x", "y")
graphtest.get_edges