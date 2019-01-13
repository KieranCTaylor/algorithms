import sys
import threading
from collections import namedtuple, deque

sys.setrecursionlimit(2 ** 20)
threading.stack_size(67108864)

problem_path = 'problem_files/toySCC.txt'

Edge = namedtuple('Edge', ['start', 'end'])

# previously completed this problem in python using global variables... now attempting
# a cleaner solution!

def main():

    adj_list, r_adj_list = open_problem_file(problem_path)

    sorted_nodes = sorted(adj_list, reverse=True)

    first_ordering = first_pass(r_adj_list, sorted_nodes)

    print(first_ordering)

    reversed_ordering = sorted(first_ordering, reverse=True)

    sccs = second_pass(adj_list, reversed_ordering)

    print(sccs)


def first_pass(adj_list, ordering):

    found_nodes = {None}
    finishing_times = deque()

    for node in ordering:

        if node not in found_nodes:

            new_finds, new_finishers = dfs(adj_list, found_nodes, finishing_times, node)

            found_nodes.update(new_finds)

    return finishing_times


def second_pass(adj_list, ordering):

    found_nodes = {None}
    finishing_times = []
    sccs = []

    for node in ordering:

        if node not in found_nodes:

            new_finds, new_finishers = dfs(adj_list, found_nodes, finishing_times, node)

            found_nodes.update(new_finds)

            sccs.append(new_finishers)

    return sccs


def dfs(adj_list, found_nodes, finishing_times, start_node=1):

    found_nodes.add(start_node)

    neighbours = adj_list[start_node]

    nodes_to_find = [x for x in neighbours if x not in found_nodes]

    for vertex in nodes_to_find:

        if vertex not in found_nodes:

            new_finds, new_finishers = dfs(adj_list, found_nodes, finishing_times, vertex)

            found_nodes.update(new_finds)

    finishing_times.append(start_node)

    return found_nodes, finishing_times


def open_problem_file(path):

    def to_adjacency_list(paths):

        vertices = set(
            sum(
                ([edge.start, edge.end] for edge in paths), []
            )
        )

        adjacency_list = {v: set() for v in vertices}

        for edge in paths:
            adjacency_list[edge.start].add(edge.end)

        return adjacency_list

    with open(path, 'r') as inp:
        inp_arr = [x.strip().split(" ") for x in inp.readlines()]

    edges = [Edge(int(x[0]), int(x[1])) for x in inp_arr]

    r_edges = [Edge(int(x[1]), int(x[0])) for x in inp_arr]

    adj_list = to_adjacency_list(edges)

    r_adj_list = to_adjacency_list(r_edges)

    return adj_list, r_adj_list


if __name__ == '__main__':

    main()
