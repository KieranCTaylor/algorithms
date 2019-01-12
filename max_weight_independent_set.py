from collections import namedtuple


Node = namedtuple('Node', ['index', 'weight'])

problem_path = 'problem_files/max_weight_independent_set.txt'

vertices_to_test = {1, 2, 3, 4, 17, 117, 517, 997}


def main():
    """
    The problem file contains the number of nodes followed by the weight of each node.
    Construct a binary string representing whether the nodes {1, 2, 3, 4, 17, 117, 517, and 997}
    are a part of the maximum weight independent set.
    """

    node_count, weights = open_problem_file(problem_path)

    nodes = [Node(index=c, weight=w) for c, w in enumerate(weights, 1)]

    max_weights = generate_max_weights(nodes)
    max_weight = max_weights[-1]

    print(f'Maximum weight sum independent set -> {max_weight}')

    max_set = generate_max_set(max_weights)

    binary_string = generate_binary_string(max_set, vertices_to_test)

    print(f'Binary string -> {binary_string}')


def open_problem_file(file_path):

    with open(file_path) as file:
        header = int(file.readline())
        data = [int(x) for x in file.readlines()]

    return header, data


def generate_max_weights(nodes):

    max_weights = [0, nodes[0].weight]

    for i, node in enumerate(nodes[1:], 2):
        next_max = max(max_weights[i-1], max_weights[i-2] + node.weight)
        max_weights.append(next_max)

    return max_weights[1:]


def generate_max_set(max_weights):

    pointer = len(max_weights) - 1

    max_set = set()

    while pointer > 0:
        if max_weights[pointer] == max_weights[pointer - 1]:
            pointer -= 1
        else:
            max_set.add(pointer)
            pointer -= 2

    return max_set


def generate_binary_string(max_set, vertices):

    binary_string = ''

    for v in vertices:
        if v in max_set:
            binary_string = binary_string + '1'
        else:
            binary_string = binary_string + '0'

    return binary_string


if __name__ == '__main__':

    main()
