from collections import namedtuple


Item = namedtuple('Item', ['value', 'weight'])

problem_paths = ['problem_files/knapsack1.txt', 'problem_files/knapsack_big.txt']


def main():
    """
    File header contains knapsack capacity and number of items.
    For both files compute the maximum value knapsack configuration.
    """

    for path in problem_paths:

        header, data = open_problem_file(path)

        knapsack_size = int(header[0])
        item_count = int(header[1])

        items = [Item(pair[0], pair[1]) for pair in data]

        filled_knapsack = knapsack(knapsack_size, items)

        print(f'Optimum solution for {path} is:\n{max(filled_knapsack[-1])}\n')


def open_problem_file(file_path):

    with open(file_path) as file:
        header = file.readline().split()
        pairs = [x.split() for x in file.readlines()]
        data = [(int(pair[0]), int(pair[1])) for pair in pairs]

    return header, data


def knapsack(knapsack_capacity, items):

    knapsacks = [[0 for _ in range(knapsack_capacity + 1)] for i in range(len(items) + 1)]

    for i in range(len(items) + 1):
        item = items[i - 1]

        for capacity in range(1, knapsack_capacity + 1):

            if i == 0 or capacity == 0:
                pass

            elif item.weight <= capacity:
                knapsacks[i][capacity] = max(
                        item.value + knapsacks[i - 1][capacity - item.weight],
                        knapsacks[i - 1][capacity]
                        )

            else:
                knapsacks[i][capacity] = knapsacks[i - 1][capacity]

    return knapsacks


if __name__ == '__main__':
    main()
