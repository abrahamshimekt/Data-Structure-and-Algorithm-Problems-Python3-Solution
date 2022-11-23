from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

class Vertex:
    vertices = {}

    def __init__(self, label):
        self.label = label

    def addVertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = 1

    def getVertices(self):
        return self.vertices


class Edge:
    edges = {}

    def __init__(self, start=None, end=None, weight=1):
        self.start = start
        self.end = end
        self.weight = weight

    def addEdge(self, start, end, weight):
        start = Vertex(start)
        end = Vertex(end)
        vertices = Vertex.vertices
        if start not in vertices:
            vertices[start.label] = 1
        if end not in vertices:
            vertices[end.label] = 1
        key1 = (start.label, end.label)
        key2 = (end.label, start.label)
        if key1 not in self.edges:
            self.edges[key1] = weight
        if key2 not in self.edges:
            self.edges[key2] = weight
        else:
            self.edges[key1] = weight
            self.edges[key2] = weight

    def getEdges(self):
        return self.edges


class Graph:
    def __init__(self):
        self.vertices = Vertex.vertices
        self.edges = Edge.edges
        self.adjacencyList = {}
        for edge in self.edges:
            if edge[0] not in self.adjacencyList:
                self.adjacencyList[edge[0]] = [edge[1]]
            else:
                self.adjacencyList[edge[0]].append(edge[1])

    def bfs(self, start, destination):
        visited = {start: 1}
        q = deque(start)
        parent = {}
        path = []
        while q:
            curr = q.popleft()
            if curr == destination:
                node = curr

                path.append(node)
                while node:
                    node = parent.get(node)
                    if node:
                        path.append(node)
                return path[::-1]
            for neighbor in self.adjacencyList[curr]:
                if neighbor not in visited:
                    visited[neighbor] = 1
                    q.append(neighbor)
                    parent[neighbor] = curr
        return path
    def dfs (self,start,destination ):
        stack = [start]
        visited = {}
        path = []
        while stack:
            curr = stack.pop()
            path.append(curr)
            if curr == destination:
                return path
            for neighbor in self.adjacencyList[curr]:
                if neighbor not in visited:
                    visited[neighbor] =1
                    stack.append(neighbor)
        return []




v = Vertex("E")
v.addVertex("A")
v.addVertex("B")
v.addVertex("C")
v.addVertex("D")
e = Edge()
e.addEdge("A", "E", 10)
e.addEdge("A", "C", 2)
e.addEdge("A", "D", 2)
e.addEdge("D", "B", 3)
e.addEdge("D", "L", 1)
e.addEdge("C", "L", 12)
e.addEdge("B", "F", 12)
e.addEdge("F", "E", 12)
G = Graph()
print(G.adjacencyList)
print(G.bfs("A","F"))
print(G.dfs("A","P"))

G2 = nx.Graph()
e = e.edges
for edge in e:
    G2.add_edge(edge[0],edge[1])
nx.draw(G2,with_labels=True)
plt.show()
