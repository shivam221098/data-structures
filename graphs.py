class Graph:
    graph_dict = {}

    def add_edge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict.update({node: [neighbour]})

        else:
            self.graph_dict.get(node).append(neighbour)

    def show_edges(self):
        edges = []

        for node in self.graph_dict:
            for neighbour in self.graph_dict.get(node):
                edges.append((node, neighbour))

        print(edges)

    def find_path(self, start, end, path=None):
        if path is None:
            path = []

        path = path + [start]

        if start == end:
            return path

        for node in self.graph_dict.get(start):
            if node not in path:
                new_path = self.find_path(node, end, path)
                if new_path:
                    return new_path
                return None


if __name__ == '__main__':
    """graph = {
        'a': ['c'],
        'b': ['c', 'e'],
        'c': ['a', 'b', 'd', 'e'],
        'd': ['c'],
        'e': ['c', 'b'],
        'f': []
    }"""

    graph = Graph()
    graph.add_edge('a', 'c')
    graph.add_edge('b', 'c')
    graph.add_edge('b', 'e')
    graph.add_edge('c', 'a')
    graph.add_edge('c', 'b')
    graph.add_edge('c', 'd')
    graph.add_edge('c', 'e')
    graph.add_edge('d', 'c')
    graph.add_edge('e', 'c')
    graph.add_edge('e', 'b')
    graph.add_edge('f', None)

    graph.show_edges()

    print(graph.find_path('a', 'e'))