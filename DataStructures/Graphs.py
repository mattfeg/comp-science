class Node:
    def __init__(self,name) -> None:
        self.name = name
        self.edges = []
        self.labels = []

class Edge:
    def __init__(self,nodeSource,nodeTarget) -> None:
        self.source = nodeSource
        self.target = nodeTarget
        self.labels = []
        self.name = [self.source.name, self.target.name]
    
class DiGraph:
    def __init__(self) -> None:
        self.nodes = []
        self.edges = []
    
    def addNode(self, name):
        node = Node(name)
        self.nodes.append(node)
    
    def removeNode(self, name):
        for node in self.nodes:
            if node.name == name:
                self.nodes.remove(node)
                
    def addEdge(self, nodeSource, nodeTarget):
        for node in self.nodes:
            if node.name == nodeSource:
                nodeSource = node
            if node.name == nodeTarget:
                nodeTarget = node
        edge = Edge(nodeSource, nodeTarget)
        nodeSource.edges.append(edge)
        nodeTarget.edges.append(edge)
        self.edges.append(edge)
        
    def showNodes(self):
        return print([node.name for node in self.nodes])
    
    def showEdges(self):
        return print([edge.name for edge in self.edges])