"""
The Bellman-Ford algorithm is a single source shortest path evaluator, like Dijkstra.
Although it runs in a slower time of O(mn) compared to Dijkstra O(m log n), it is able to detect negative
edge cycles and can run in a distributed fashion, making it useful for internet routing.
"""
from collections import namedtuple
import sys


Edge = namedtuple('Edge', ['start_node', 'end_node', 'weight'])

problem_paths = ['problem_files/g1.txt', 'problem_files/g2.txt', 'problem_files/g3.txt']

INF = sys.maxsize


def main():
    """
    Given the edges in the problem files, find first if a negative edge cycle exists,
    if not, return the shortest of all paths from any s -> v
    (also achieved using Floyd-Warshall, could be sped up by using Dijkstra once no negative cycles been confirmed)
    """

    for path in problem_paths:

        edges = open_problem_file(path)
        nodes = find_all_nodes(edges)

        source_nodes = nodes.copy()
        source = source_nodes.pop()

        min_paths, negative_cycles = bellman_ford(edges, nodes, source)

        if not negative_cycles:
            print(f'No negative cycles for problem {path}, now calculating all path distances...')
            shortest_path = min(min_paths.values())

            for i in range(len(source_nodes)):

                source = source_nodes.pop()

                min_paths, negative_cycles = bellman_ford(edges, nodes, source)
                shortest_path = min(
                    min(min_paths.values()),
                    shortest_path
                )

            print(f'Shortest path is {shortest_path}')

        else:
            print(f'Negative edge detected for {path}')


def bellman_ford(edges, nodes, source):

    shortest_path_to = {node: INF for node in nodes}

    shortest_path_to[source] = 0

    for i in range(len(nodes) - 1):

        for edge in edges:

            current_distance = shortest_path_to[edge.end_node]
            distance_using_source = shortest_path_to[edge.start_node] + edge.weight

            shortest_distance = min(
                current_distance,
                distance_using_source
            )

            shortest_path_to[edge.end_node] = shortest_distance

    negative_cycles = detect_negative_cycles(shortest_path_to, edges)

    return shortest_path_to, negative_cycles


def detect_negative_cycles(shortest_path_to, edges):

    negative_cycles = False

    for edge in edges:
        current_distance = shortest_path_to[edge.end_node]
        distance_using_source = shortest_path_to[edge.start_node] + edge.weight

        if current_distance > distance_using_source:
            negative_cycles = True

    return negative_cycles


def find_all_nodes(edges):

    nodes = set()

    for edge in edges:
        nodes.add(edge.start_node)
        nodes.add(edge.end_node)

    return nodes


def open_problem_file(path):

    edges = []

    with open(path) as file:
        header = file.readline()
        for line in file:
            data = line.strip().split()
            edges.append(Edge(data[0], data[1], int(data[2])))

    return edges


if __name__ == '__main__':

    main()
