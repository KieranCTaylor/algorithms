from collections import namedtuple, deque
import sys


INF = sys.maxsize
Edge = namedtuple('Edge', ['start_node', 'end_node', 'weight'])

problem_path = 'problem_files/dijkstra.txt'


def main():
    pass


class Graph(object):

    def __init__(self, input_edges):
        self.edges = {Edge(*edge) for edge in input_edges}
        self.costs = {(x.start_node, x.end_node): x.weight for x in self.edges}

    @property
    def vertices(self):
        nodes = set()

        for edge in self.edges:
            nodes.add(edge.start_node)
            nodes.add(edge.end_node)

        return nodes

    def get_neighbours(self, edge):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

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
