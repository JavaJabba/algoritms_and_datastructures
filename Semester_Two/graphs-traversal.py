
""" Sample solutions to Lab on implementing the Graph ADT and DFS/BFS.

    Implements the graph as a map of (vertex,edge-map) pairs.
"""

#needed for searching using a stack
# my implementation of a stack using a python list, from CS2515
from stack import Stack

import copy

class Vertex:
    """ A Vertex in a graph. """
    
    def __init__(self, element):
        """ Create a vertex, with data element. """
        self._element = element

    def __str__(self):
        """ Return a string representation of the vertex. """
        return str(self._element)

    def __lt__(self, v):
        """ Return true if this object is less than v.
       
        Args:
            v -- a vertex object
        """
        return self._element < v.element()

    def element(self):
        """ Return the data for the vertex. """
        return self._element
    
class Edge:
    """ An edge in a graph.

    Implemented with an order, so can be used for directed or undirected
    graphs. Methods are provided for both. It is the job of the Graph class
    to handle them as directed or undirected.
    """
    
    def __init__(self, v, w, element):
        """ Create an edge between vertices v and w, with label element.

        Args:
            element -- the label, can be an arbitrarily complex structure.
        """
        self._vertices = (v,w)
        self._element = element

    def __str__(self):
        """ Return a string representation of this edge. """
        return ('(' + str(self._vertices[0]) + '--'
                   + str(self._vertices[1]) + ' : '
                   + str(self._element) + ')')

    def vertices(self):
        """ Return an ordered pair of the vertices of this edge. """
        return self._vertices

    def start(self):
        """ Return the first vertex in the ordered pair. """
        return self._vertices[0]

    def end(self):
        """ Return the second vertex in the ordered. pair. """
        return self._vertices[1]

    def opposite(self, v):
        """ Return the opposite vertex to v in this edge. """
        if self._vertices[0] == v:
            return self._vertices[1]
        elif self._vertices[1] == v:
            return self._vertices[0]
        else:
            return None

    def element(self):
        """ Return the data element for this edge. """
        return self._element

class Graph:
    """ Represent a simple graph.

        This version maintains only undirected graphs, and assumes no
        self loops.
    """

    #Implement as a Python dictionary
    #  - the keys are the vertices
    #  - the values are the edge sets for that vertex
    #         Each edge set is also maintained as a dictionary,
    #         with opposite vertex as the key and the edge object as the value
    
    def __init__(self):
        """ Create an initial empty graph. """
        self._structure = dict()

    def __str__(self):
        """ Return a string representation of the graph. """
        hstr = ('|V| = ' + str(self.num_vertices())
                + '; |E| = ' + str(self.num_edges()))
        vstr = '\nVertices: '
        for v in self._structure:
            vstr += str(v) + '-'
        edges = self.edges()
        estr = '\nEdges: '
        for e in edges:
            estr += str(e) + ' '
        return hstr + vstr + estr

    #--------------------------------------------------#
    #ADT methods to query the graph
    
    def num_vertices(self):
        """ Return the number of vertices in the graph. """
        return len(self._structure)

    def num_edges(self):
        """ Return the number of edges in the graph. """
        num = 0
        for v in self._structure:
            num += len(self._structure[v])    #the dict of edges for v
        return num //2     #divide by 2, since each edege appears in the
                           #vertex list for both of its vertices

    def vertices(self):
        """ Return a list of all vertices in the graph. """
        return [key for key in self._structure]

    def get_vertex_by_label(self, element):
        """ get the first vertex that matches element. 
        
        Beware - this method is inefficient, and will be really noticeable
        if used on large graphs.
        """
        for v in self._structure:
            if v.element() == element:
                return v
        return None

    def edges(self):
        """ Return a list of all edges in the graph. """
        edgelist = []
        for v in self._structure:
            for w in self._structure[v]:
                #to avoid duplicates, only return if v is the first vertex
                if self._structure[v][w].start() == v:
                    edgelist.append(self._structure[v][w])
        return edgelist

    def get_edges(self, v):
        """ Return a list of all edges incident on v.

        Args:
            v -- a vertex object
        """
        if v in self._structure:
            edgelist = []
            for w in self._structure[v]:
                edgelist.append(self._structure[v][w])
            return edgelist
        return None

    def get_edge(self, v, w):
        """ Return the edge between v and w, or None, if there is no edge.

        Args:
            v -- a Vertex object
            w -- a Vertex object
        """
        if (self._structure != None
                         and v in self._structure
                         and w in self._structure[v]):
            return self._structure[v][w]
        return None

    def degree(self, v):
        """ Return the degree of vertex v. """
        return len(self._structure[v])

    #--------------------------------------------------#
    #ADT methods to modify the graph
    
    def add_vertex(self, element):
        """ Add and return a new vertex with data element.

        Note -- if there is already a vertex with the same data element,
        this will create another vertex instance with the same element.
        If the client using this ADT implementation does not want these 
        duplicates, it is the client's responsibility not to add duplicates.
        """
        v = Vertex(element)
        self._structure[v] = dict()  # create an empty dict, ready for edges
        return v

    def add_vertex_if_new(self, element):
        """ Add and return a vertex with element, if not already in graph.

        Checks for equality between the elements. If there is special
        meaning to parts of the element (e.g. element is a tuple, with an
        'id' in cell 0), then this method may create multiple vertices with
        the same 'id' if any other parts of element are different.

        To ensure vertices are unique for individual parts of element,
        separate methods need to be written.

        Beware -- this will be inefficient for large graphs.
        """
        for v in self._structure:
            if v.element() == element:
                #print('Already there')
                return v
        return self.add_vertex(element)

    def add_edge(self, v, w, element):
        """ Add and return an edge, with element, between two vertices v and w.

        If either v or w are not vertices in the graph, does not add, and
        returns None.
            
        If an edge already exists between v and w, this will
        replace the previous edge.
        """
        if not v in self._structure or not w in self._structure:
            return None
        e = Edge(v, w, element)
        # self._structure[v] is the dictionary of v's edges
        # so need to insert an entry for key w, with value e
        # A clearer way of expressing it would be
        # v_edges = self._structure[v]
        # v_edges[w] = e
        self._structure[v][w] = e  
        self._structure[w][v] = e
        return e

    def add_edge_pairs(self, elist):
        """ Add all vertex pairs in elist as edges with empty elements. """
        for (v,w) in elist:
            self.add_edge(v,w,None)

    #--------------------------------------------------#
    #Additional methods to explore the graph
        
    def highestdegreevertex(self):
        """ Return the vertex with highest degree. """
        hd = -1
        hdv = None
        for v in self._structure:
            if self.degree(v) > hd:
                hd = self.degree(v)
                hdv = v
        return hdv            

    # --------------------------------------------------#
    # Traversal methods
    
    def dfs_stack(self, v):
        """ Return a DFS tree from v, using a stack.        """
        marked = {}
        stack = Stack()
        stack.push((v,None))
        # print('   pushed', v, 'from None')
        while stack.length() > 0:
            (vertex,edge) = stack.pop()
            if vertex not in marked:
                # print('popped unvisited', vertex)
                marked[vertex] = edge
                for e in self.get_edges(vertex):
                    w = e.opposite(vertex)
                    stack.push((w,e))
                    # print('   pushed', w, 'from', e)
        return marked

    def depthfirstsearch(self, v):
        """ Return a DFS tree from v. """
        marked = {v:None}
        self._depthfirstsearch(v, marked)
        return marked

    def _depthfirstsearch(self, v, marked):
        """ Do a recursive DFS from v, storing nodes in marked. """
        for e in self.get_edges(v):
            w = e.opposite(v)
            if w not in marked:
                marked[w] = e
                self._depthfirstsearch(w, marked)
                
    def breadthfirstsearch(self, v):
        """ Return a BFS tree from v. """
        marked = {v:None}
        level = [v]
        while len(level) > 0:
            nextlevel = []
            for w in level:
                for e in self.get_edges(w):
                    x = e.opposite(w)
                    if x not in marked:
                        marked[x] = e
                        nextlevel.append(x)
            level = nextlevel
        return marked

    def BFS_length(self, v):
        """ Return a BFS tree from v, with path lengths. 
        
        In the returned dictionary, each vertex (key) stores its parent (value).
        """
        marked = {v:(None,0)}
        level = [v]
        levelint = 1
        while len(level) > 0:
            nextlevel = []
            for w in level:
                for e in self.get_edges(w):
                    x = e.opposite(w)
                    if x not in marked:
                        marked[x] = (w, levelint)
                        nextlevel.append(x)
            level = nextlevel
            levelint += 1
        return marked
    
    def breadthfirstsearchtree(self, v):
        """ Return a down-directed BFS tree from v. 
        
        In the returned dictionary, each vertex (key) stores a list of its edge 'children'.
        """
        marked = {v:[]}
        level = [v]
        while len(level) > 0:
            nextlevel = []
            for w in level:
                for e in self.get_edges(w):
                    x = e.opposite(w)
                    if x not in marked:
                        marked[x] = []
                        marked[w].append(x)
                        nextlevel.append(x)
            level = nextlevel
        return marked

    #End of class definition

#---------------------------------------------------------------------------#
#Test methods

def test_graph():
    """ Test on a simple 3-vertex, 2-edge graph. """
    graph = Graph()
    a = graph.add_vertex('a')
    b = graph.add_vertex('b')
    c = graph.add_vertex('c')
    d = graph.add_vertex_if_new('b')   #should not create a vertex
    eab = graph.add_edge(a, b, 2)
    ebc = graph.add_edge(b,c,9)

    vnone = Vertex('dummy')
    evnone = graph.add_edge(vnone, c, 0)   #should not create an edge
    if evnone is not None:
        print('ERROR: attempted edges  should have been none')

    edges = graph.get_edges(vnone)     #should be None: vnone not in graph
    if edges != None:
        print('ERROR: returned edges for non-existent vertex.')
        
    print('number of vertices:', graph.num_vertices())
    print('number of edges:', graph.num_edges())

    print('Vertex list should be a,b,c in any order :')
    vertices = graph.vertices()
    for key in vertices:
        print(key.element())
    print('Edge list should be (a,b,2),(b,c,9) in any order :')
    edges = graph.edges()
    for edge in edges:
        print(edge)

    print('Graph display should repeat the above:')
    print(graph)

    v = graph.add_vertex('d')
    edges = graph.get_edges(v)
    if edges != []:
        print('ERROR: should have returned an empty list, but got', edges)
    print('Graph should now have a new vertex d with no edges')
    print(graph)


def get_path(v, tree):
    """ Extract a path from root to v, from backwards search tree. """
    s = Stack()
    s.push(v)
    _get_path(v, tree, s)
    return s

def _get_path(v, tree, stack):
    """ Extract a path from root to v in tree, and add to stack. """
    previous = tree[v][0]
    if previous != None:
        stack.push(previous)
        _get_path(previous, tree, stack) 
    
def test_graph2():
    """ Test Graph with the standard 6-vertex graph from lectures. """
    graph = Graph()
    a = graph.add_vertex('a')
    b = graph.add_vertex('b')
    c = graph.add_vertex('c')
    d = graph.add_vertex('d')
    e = graph.add_vertex('e')
    f = graph.add_vertex('f')
    graph.add_edge(a,b,1)
    graph.add_edge(a,c,1)
    graph.add_edge(b,c,1)
    graph.add_edge(b,d,1)
    graph.add_edge(b,e,1)
    graph.add_edge(c,f,1)
    graph.add_edge(e,f,1)

    print('Graph:')
    print(graph)
    print()
    hdv = graph.highestdegreevertex()
    print(hdv.element(),
          'has the highest degree =',
          graph.degree(hdv))
    print()

    #DFS from a, print the search tree (as a map)
    source = a
    vlist = graph.depthfirstsearch(source)
    print('The result of a depth-first traversal from:', source)
    print('Note: the 1s are the weights on the edges')
    print('Note: the DFS tree is maintained as a dict, and items appear in random order')
    print('Note: each edge is printed with vertices in the order specified on creation')
    for key in vlist:
        print(key, vlist[key])
    print()

    #Obtain transitive closure, print the edges
    print('The result of a transitive closure:')
    print('Note: as above, items appear in random order')
    print('This was a connected graph, so should get 0.5*(n-1)*n edges')
    closure = graph.transitiveclosure()
    edges = closure.edges()
    for e in edges:
        print(e)
    print()

    #BFS, augmenting search tree with path lengths, print the paths
    source = a
    print('The result of a breadth-first traversal from:', source)
    print('For each vertex, print the path from the source', source)
    print('Again, the tree is maintained in a dict, so vertices in random order')
    tree = graph.BFS_length(source)
    for v in tree:
        path = get_path(v, tree)
        print(v, '(', end='')
        while path.length() > 0:
            print(path.pop(), '', end='')
        print('):', tree[v][1])
    #Now find the deepest node
    furthest = a
    maxlength = 0
    for v in tree:
        if tree[v][1] > maxlength:
            furthest = v
            maxlength = tree[v][1]
    print('The max length from a was', maxlength, 'to', furthest)

def test_graph3():
    """ Test on the larger graph from lectures. """
    graph = Graph()
    a = graph.add_vertex('a')
    b = graph.add_vertex('b')
    c = graph.add_vertex('c')
    d = graph.add_vertex('d')
    e = graph.add_vertex('e')
    f = graph.add_vertex('f')
    g = graph.add_vertex('g')
    h = graph.add_vertex('h')
    i = graph.add_vertex('i')
    j = graph.add_vertex('j')
    k = graph.add_vertex('k')
    l = graph.add_vertex('l')
    m = graph.add_vertex('m')
    graph.add_edge(a,b,1)
    graph.add_edge(a,e,1)
    graph.add_edge(a,h,1)
    graph.add_edge(b,c,1)
    graph.add_edge(b,e,1)
    graph.add_edge(c,d,1)
    graph.add_edge(c,g,1)
    graph.add_edge(d,f,1)
    graph.add_edge(e,f,1)
    graph.add_edge(e,k,1)
    graph.add_edge(f,i,1)
    graph.add_edge(g,j,1)
    graph.add_edge(h,m,1)
    graph.add_edge(i,j,1)
    graph.add_edge(i,k,1)
    graph.add_edge(j,l,1)
    graph.add_edge(k,l,1)
    graph.add_edge(k,m,1)

    hdv = graph.highestdegreevertex()
    print(hdv.element(),
          'has the highest degree =',
          graph.degree(hdv))
    print(graph)

    vlist = graph.depthfirstsearch(c)
    for key in vlist:
        print(key, vlist[key])

    print('Depth first search:')
    vlist = graph.depthfirstsearch(hdv)
    for key in vlist:
        print(key, vlist[key])
        
    print('Breadth first search:')
    vlist = graph.breadthfirstsearch(hdv)
    for key in vlist:
        print(key, vlist[key])
        
    print('Breadth first search tree:')
    vlist = graph.breadthfirstsearchtree(hdv)
    for key in vlist:
        print(key, ':', end='')
        for x in vlist[key]:
            print(x, '', end='')
        print()
        
    print('Depth first search using a stack:')
    vlist = graph.dfs_stack(hdv)
    for key in vlist:
        print(key, vlist[key])


def printBFStree(tree):
    """ Print out a BFS tree with paths. """
    for v in tree:
        path = get_path(v, tree)
        print(v, '(', end='')
        while path.length() > 0:
            print(path.pop(), '', end='')
        print('):', tree[v][1])


def read_dolphin_graph():
    """ Read the dolphins file, return the graph and separate names dict. """
    graph = Graph()
    file = open('dolphins.gml', 'r')
    names = dict()
    file.readline() #the header with author details
    file.readline() #the start of the graph
    file.readline() #the opening square bracket
    file.readline() #the comment that the graph is not directed
    wordlist = file.readline().split()
    while wordlist[0] != ']':
        if wordlist[0] == 'node':
            file.readline() #open bracket
            nodeid = int(file.readline().split()[1])
            vertex = graph.add_vertex(nodeid)
            names[nodeid] = file.readline().split()[1]
            #print('added vertex', vertex, 'with label', names[nodeid])
            file.readline() #close bracket
        elif wordlist[0] == 'edge':
            file.readline() #open bracket
            source = int(file.readline().split()[1])
            target = int(file.readline().split()[1])
            sv = graph.get_vertex_by_label(source)
            tv = graph.get_vertex_by_label(target)
            edge = graph.add_edge(sv, tv, 1)
            #print('added edge, source =', source, '; target =', target, ':', edge)
            file.readline()
        else:
            print('ERROR: unrecognised line:', wordlist[0])
        wordlist = file.readline().split()
    return graph,names

def process_dolphins():
    """ Process the dolphin graph. """
    graph,names = read_dolphin_graph()
    print('Graph has', graph.num_vertices(), 'vertices.')
    print('Graph has', graph.num_edges(), 'edges.')
    for v in sorted(graph.vertices()):
        print(v, names[v.element()], '; deg =', graph.degree(v))

    #Now find the most central node, using 'graph centrality'
    #i.e. find the node with minimal path length to each other node

    #Use a map, with vertices as keys. For each vertex, find the shortest
    #path to each other vertex. Store the largest of these as the value
    #in the map.
    maxlengths = dict()
    
    #minmax will store the minimum max length minimum path
    #i.e. the minimum value in the dictionary
    minmax = graph.num_vertices()     #default start, actual maxlength
                                      #will be smaller for each vertex
    central_length = None             #Will be central element
    for v in graph.vertices():
        tree = graph.BFS_length(v)   #build a BFS tree with path lengths
        maxlength = 0
        for w in tree:               #find max length in the tree
            if tree[w][1] > maxlength:
                maxlength = tree[w][1]
        maxlengths[v] = maxlength    #store it in the map
        if maxlength < minmax:       #if it was better than best, update
            central_length = v
            minmax = maxlength

    #print out all vertices
    print()
    print('ID Name : Centrality')
    for v in sorted(maxlengths.keys()):
        print(v, names[v.element()], ':', maxlengths[v])
    # for k,value in sorted(maxlengths.items(), key=lambda item: item[1]):
        # print(k, names[v.element()], ':', value)

    #print out the central element
    print('The lowest graph centrality value is', minmax)
    print('The (equal) central dolphin, by graph centrality, is',
           central_length,
          '(', names[central_length.element()], ')')

    #For comparison, print out element with highest degree.
    hdv = graph.highestdegreevertex()
    print(hdv.element(),
          '(', names[hdv.element()], ')' 
          'has the highest degree =',
          graph.degree(hdv))
        
def read_usa_graph():
    """ Read and return the graph of contiguous USA states. """
    graph = Graph()
    file = open('contiguous-usa.txt', 'r')
    count = 0
    for line in file:
        pair = line.split()
        state1 = pair[0]
        state2 = pair[1]
        v1 = graph.add_vertex_if_new(state1)
        v2 = graph.add_vertex_if_new(state2)
        graph.add_edge(v1, v2, 1)
        count += 1
    file.close()
    return graph

def process_usa():
    """ Process the USA graph. """
    graph = read_usa_graph()
    print('Graph has', graph.num_vertices(), 'vertices.')
    print('Graph has', graph.num_edges(), 'edges.')

    #Now find the most central node, using 'graph centrality'
    #i.e. find the node with minimal path length to each other node

    #Use a map, with vertices as keys. For each vertex, find the shortest
    #path to each other vertex. Store the largest of these as the value
    #in the map.
    maxlengths = dict()
    
    #minmax will store the minimum max length minimum path
    #i.e. the minimum value in the dictionary
    minmax = graph.num_vertices()     #default start, actual maxlength
                                      #will be smaller for each vertex
    central_length = None             #Will be central element
    for v in graph.vertices():
        tree = graph.BFS_length(v)   #build a BFS tree with path lengths
        maxlength = 0
        for w in tree:               #find max length in the tree
            if tree[w][1] > maxlength:
                maxlength = tree[w][1]
        maxlengths[v] = maxlength    #store it in the map
        if maxlength < minmax:       #if it was better than best, update
            central_length = v
            minmax = maxlength

    #print out all vertices
    print()
    print('State : Centrality')
    for v in sorted(maxlengths.keys()):
        print(v, ':', maxlengths[v])
    # for k,value in sorted(maxlengths.items(), key=lambda item: item[1]):
        # print(k, ':', value)


    #print out the central element
    print('The lowest graph centrality value is', minmax)
    print('The (equal) central state, by graph centrality, is',
           central_length)

    #For comparison, print out element with highest degree.
    hdv = graph.highestdegreevertex()
    print(hdv.element(),
          'has the highest degree =',
          graph.degree(hdv))


# *******************************************************************

# process_usa()
#process_dolphins()
test_graph()
    
