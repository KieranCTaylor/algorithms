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

        print(f'Optimum solution for {path} is:\n{max(filled_knapsack)}\n')


def open_problem_file(file_path):

    with open(file_path) as file:
        header = file.readline().split()
        pairs = [x.split() for x in file.readlines()]
        data = [(int(pair[0]), int(pair[1])) for pair in pairs]

    return header, data


def knapsack(knapsack_size, items):

    dynamic_solutions = [0 for x in range(knapsack_size + 1)]

    for item_pointer in range(len(items) + 1):

        for current_capacity in range(knapsack_size+1):

            if item_pointer == 0 or current_capacity == 0:
                pass

            else:
                current_item = items[item_pointer - 1]

                if current_item.weight <= current_capacity:

                    max_value_with_remaining_capacity = dynamic_solutions[current_capacity - current_item.weight]
                    max_value_with_current_item = current_item.value + max_value_with_remaining_capacity

                    max_value_without_current_item = dynamic_solutions[current_capacity]

                    dynamic_solutions[current_capacity] = max(max_value_with_current_item,
                                                              max_value_without_current_item)

    return dynamic_solutions


if __name__ == '__main__':
    main()
