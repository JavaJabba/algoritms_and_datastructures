'''
Graphs

Algorithms and Data Structures II
Dylan Murray 121747725

'''
class GraphADT:

    def __init__(self, adjList):
        self._adjlist = adjList
        self._adjList = {"A":["B", "C"], "B":["A", "C", "E", "D"], "C":["A", "B", "F"], "D":["B"], "E":["B", "F"], "F":["C", "E"]}

    class Vertex:
        def __init__(self, element):
            self._element = element

        def __str__(self):
            return str(self._element)
        
        def element(self):
            return self._element
    
    class Edge:

        def __init__(self, xVertex, yVertex):
            self._xVertex = xVertex
            self._yVertex = yVertex

        def vertices(self):
            pass
        
        def opposite(self, x):
            pass

        def element(self):
            pass

        def __str__(self):
            pass