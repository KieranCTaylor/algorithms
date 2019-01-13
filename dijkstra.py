from collections import namedtuple, deque
import sys


INF = sys.maxsize
Edge = namedtuple('Edge', ['start_node', 'end_node', 'weight'])

problem_path = 'problem_files/dijkstra.txt'

paths_to_find = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]


def main():
    """
    Given graph input as an adjacency list, calculate the shortest path distance
    to a list of given vertices. (parts of solution inspired by Maria Boldyreva @dev.to)
    """

    adjacency_list = make_adjacency_list_from(problem_path)

    input_graph = Graph(adjacency_list)

    shortest_paths = dijkstra(input_graph, '1')

    for n in paths_to_find:

        node = str(n)

        path_to_node = shortest_paths[node]

        print(f'Shortest path to {node} -> {path_to_node}')

        path_distances = []
        for i in range(len(path_to_node) - 1):
            edge_weight = input_graph.weights[(path_to_node[i], path_to_node[i + 1])]
            path_distances.append(edge_weight)

        print(f'Weight of path: {sum(path_distances)}\n')


def dijkstra(graph, source):

    nodes_to_visit = graph.vertices.copy()

    distance_to = {v: INF for v in nodes_to_visit}
    distance_to[source] = 0

    path_history = {v: None for v in nodes_to_visit}

    visited = {source}

    while len(visited) < len(graph.vertices):

        closest_vertex = min(nodes_to_visit, key=lambda v: distance_to[v])

        new_neighbours = graph.get_neighbours(closest_vertex)

        for neighbour, weight in new_neighbours:

            distance_from_neighbour = distance_to[closest_vertex] + weight

            if distance_from_neighbour < distance_to[neighbour]:
                distance_to[neighbour] = distance_from_neighbour
                path_history[neighbour] = closest_vertex

        nodes_to_visit.remove(closest_vertex)
        visited.add(closest_vertex)

    return build_shortest_paths(source, graph.vertices, path_history)


def build_shortest_paths(source, vertices, path_history):

    shortest_paths = {v: deque() for v in vertices}
    shortest_paths[source].appendleft(0)

    for destination in vertices:
        path, current_vertex = shortest_paths[destination], destination
        node_history = path_history.copy()

        while node_history[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = node_history[current_vertex]
        if path:
            path.appendleft(current_vertex)

    return shortest_paths


class Graph(object):

    def __init__(self, input_edges):
        self.edges = {Edge(*edge) for edge in input_edges}
        self.weights = {(x.start_node, x.end_node): x.weight for x in self.edges}

    @property
    def vertices(self):
        nodes = set()

        for edge in self.edges:
            nodes.add(edge.start_node)
            nodes.add(edge.end_node)

        return nodes

    def get_neighbours(self, vertex):

        neighbours = set()

        for edge in self.edges:
            if edge.start_node == vertex:
                neighbours.add((edge.end_node, edge.weight))
            elif edge.end_node == vertex:
                neighbours.add((edge.start_node, edge.weight))

        return neighbours

    def subtract_edge(self, start_node, end_node):

        for edge in self.edges:
            if edge.start_node == start_node and edge.end_node == end_node:
                self.edges.remove(edge)

    def add_edge(self, start_node, end_node, weight):

        new_edge = Edge(start_node, end_node, weight)
        self.edges.add(new_edge)


def make_adjacency_list_from(path):
    # hacky way of parsing file, but it does the job and input is static

    with open(path, 'r') as file:
        input_array = [x.strip().replace("\t\t", "\t").split("\n") for x in file.readlines()]

    new_arr = []

    for line in input_array:
        pairing = line[0].split()
        pairings = [(pairing[0], x.split(",")[0], int(x.split(",")[1])) for x in pairing[1:]]
        new_arr.extend(pairings)

    print("Reading input complete!")

    return new_arr


if __name__ == '__main__':

    main()
