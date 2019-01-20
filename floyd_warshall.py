from collections import namedtuple
import sys


Edge = namedtuple('Edge', ['start_node', 'end_node', 'weight'])

problem_paths = ['problem_files/g1.txt', 'problem_files/g2.txt', 'problem_files/g3.txt']

INF = sys.maxsize


def main():

    for path in problem_paths:

        edges = open_problem_file(path)
        min_paths, negative_cycles = floyd_warshall(edges)

        if not negative_cycles:
            print(min([min(min_paths[x]) for x in min_paths]))


def floyd_warshall(edges):

    nodes = find_all_nodes(edges)

    min_paths = {node: {v: INF for v in nodes} for node in nodes}

    for edge in edges:
        min_paths[edge.start_node][edge.end_node] = edge.weight

    for node in nodes:
        min_paths[node][node] = 0

    for intermediate in nodes:
        for source in nodes:
            for dest in nodes:

                current_weight = min_paths[source][dest]
                min_weight = min(
                    current_weight,
                    min_paths[source][intermediate] + min_paths[intermediate][dest]
                )

                min_paths[source][dest] = min_weight

    result, negative_cycles_exist = detect_negative_cycles(min_paths)

    return result, negative_cycles_exist


def detect_negative_cycles(min_paths):

    negative_cycles = False

    for node in min_paths:

        if min_paths[node][node] < 0:
            print('Negative cycle detected!')
            negative_cycles = True
            return min_paths, negative_cycles

        else:
            min_paths[node][node] = INF

    return min_paths, negative_cycles


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
