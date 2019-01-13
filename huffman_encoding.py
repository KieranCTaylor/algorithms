import heapq
from collections import namedtuple


TreeNode = namedtuple('TreeNode', ['freq', 'key', 'left', 'right'])

problem_path = 'problem_files/huffman.txt'


def main():
    """
    Given a frequency list, construct a huffman encoding tree with optimal space usage.
    Find the minimum and maximum length of code in resulting tree.
    """

    huffman_tree = construct_tree(read_input(problem_path))

    codes = assign_codes(root=huffman_tree[0])

    lengths = [len(x) for x in codes.values()]

    print(f'Max length of code: {max(lengths)}')
    print(f'Min length of code: {min(lengths)}')


def construct_tree(freq_dict):

    heap = []

    for key in freq_dict:
        node = TreeNode(freq_dict[key], key, None, None)
        heapq.heappush(heap, node)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = TreeNode(left.freq + right.freq, None, left, right)

        heapq.heappush(heap, merged)

    return heap


def assign_codes(root, code=""):

    codes = {}

    if root is not None:

        if root.key is not None:
            codes[root.key] = code

        codes.update(assign_codes(root.left, code + "0"))
        codes.update(assign_codes(root.right, code + "1"))

    return codes


def read_input(path):

    with open(path, 'r') as data_file:
        header = data_file.readline()
        frequency_dict = {x: int(x) for x in data_file.readlines()}

    return frequency_dict


if __name__ == '__main__':

    main()
