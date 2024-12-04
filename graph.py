import sys
class Graph:
    class Vertex:
        def __init__(self, id):
            self.vertex_id = id
            self.neighborlist = {}
        
        def isNeighbor(self, id):
            return id in self.neighborlist
        
        def addNeighbor(self, id, weight=0):
            if not self.isNeighbor(id):
                self.neighborlist[id] = weight
        
        def listNeighbors(self):
            return self.neighborlist.keys()
        
        def edgeCost(self, id):
            if id in self.neighborlist:
                return self.neighborlist[id]
            else:
                return sys.maxsize
    
    def __init__(self):
        self.vertexcount = 0
        self.adjacencylist = {}
    
    def getVertexCount(self):
        return self.vertexcount
    
    def addVertex(self, id):
        if not id in self.adjacencylist:
            newVertex = self.Vertex(id)
            self.adjacencylist[id] = newVertex
            self.vertexcount += 1
    
    def addEdge(self, frm, to, wt = 0):
        if not frm in self.adjacencylist:
            self.addVertex(frm)
        if not to in self.adjacencylist:
            self.addVertex(to)
        self.adjacencylist[frm].addNeighbor(to, wt)
        self.adjacencylist[to].addNeighbor(frm, wt)
        
    def getEdgeCost(self, frm, to):
        if frm in self.adjacencylist and to in self.adjacencylist:
            return self.adjacencylist[frm].edgeCost(to)
        
    def getVertexList(self):
        return list(self.adjacencylist.keys())
    
    def getNeighbors(self, id):
        if id in self.adjacencylist:
            return self.adjacencylist[id].listNeighbors()
        else:
            return None
        
    def printGraph(self):
        for vertex in self.adjacencylist:
            print(vertex, "->", self.adjacencylist[vertex].listNeighbors())
            
    def getFirstPath(self, start,end, path = []):
        if not start in self.getVertexList():
            return None
        path = path + [start]
        if start == end:
            return path
        for node in self.getNeighbors(start):
            if node not in path:
                newpath = self.getFirstPath(node, end, path)
                if newpath:
                    return newpath
        return None        

# Test the graph class
g = Graph()
g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.addVertex(7)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 4)
g.addEdge(0, 3, 2)
g.addEdge(1, 4, 4)
g.addEdge(1, 5, 3)
g.addEdge(2, 6, 1)
g.addEdge(3, 7, 3)
g.printGraph()
print(g.getEdgeCost(0, 1))
print(g.getEdgeCost(0, 3))
print(g.getFirstPath(0, 5))

# Output
# 0 -> dict_keys([1, 2, 3])
# 1 -> dict_keys([0, 4, 5])
# 2 -> dict_keys([0, 6])
# 3 -> dict_keys([0, 7])
# 4 -> dict_keys([1])
# 5 -> dict_keys([1])
# 6 -> dict_keys([2])
# 7 -> dict_keys([3])
# 5
# 2
# 3
# 1
# 3
# 4
# 3
# 1
# 1
# 2
# 3

            
        