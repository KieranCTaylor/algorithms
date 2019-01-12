from collections import namedtuple


problem_path = 'problem_files/clustering1.txt'

Edge = namedtuple('Edge', ['start_node', 'end_node', 'weight'])

k = 4


def main():

    header, data = open_problem_file(problem_path)

    edges = sorted([Edge(int(edge[0]), int(edge[1]), int(edge[2])) for edge in data], key=lambda x: int(x.weight))

    vertices = set()

    for e in edges:
        vertices.add(e.start_node)
        vertices.add(e.end_node)

    union_find = UnionFind(vertices)

    mst = []

    for edge in edges:

        if not union_find.forms_cycle(edge.start_node, edge.end_node):
            mst.append(edge)
            union_find.union(edge.start_node, edge.end_node)

    mst_edge_lengths = [x.weight for x in mst]

    min_distance_between_k_clusters = sorted(mst_edge_lengths, reverse=True)[k - 2]

    print(min_distance_between_k_clusters)


class UnionFind(object):

    def __init__(self, nodes):

        self.leaders = {node: node for node in nodes}

    def find(self, member):

        return self.leaders[member]

    def union(self, i, j):

        i_leader = self.find(i)
        j_leader = self.find(j)

        i_cluster = [x for x in self.leaders if self.leaders[x] == i_leader]
        j_cluster = [x for x in self.leaders if self.leaders[x] == j_leader]

        if i_cluster > j_cluster:
            new_leader, small_cluster = i_leader, j_cluster
        else:
            new_leader, small_cluster = j_leader, i_cluster

        for member in small_cluster:
            self.leaders[member] = new_leader

    def forms_cycle(self, i, j):

        i_leader = self.find(i)
        j_leader = self.find(j)

        return i_leader == j_leader


def open_problem_file(file_path):

    with open(file_path) as file:
        header = file.readline()
        data = [x.strip().split() for x in file.readlines()]

    return header, data


if __name__ == '__main__':
    main()
