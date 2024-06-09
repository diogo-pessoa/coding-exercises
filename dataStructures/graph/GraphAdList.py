class GraphAdjList:
    """
    Watching spider-man across the spider-verse as I study this. Hard not to use it
    as a reference for this graph implementation. :P
    """

    def __init__(self):
        self.graph = {}

    def add_canon_event(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_connection(self, vertex1, vertex2):
        # Check if vertex1 and vertex2 are in the graph
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
            return True
        return False

    def remove_connection(self, vertex1, vertex2):
        # Check if vertex1 and vertex2 are in the graph
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)
            return True
        return False

    def remove_canon_event(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for key in self.graph:
                if vertex in self.graph[key]:
                    self.graph[key].remove(vertex)
            return True
        return False

    def show_multiverse(self):
        for vertex in self.graph:
            print(vertex, end=" -> ")
            print(" -> ".join([str(i) for i in self.graph[vertex]]))
