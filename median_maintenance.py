from heapq import heappush, heappop, nlargest, nsmallest


problem_path = 'problem_files/median.txt'


def main():
    """
    Using two heaps, maintain a median value and sum up the cumulative median
    """

    data = open_problem_file(problem_path)

    low_heap = []
    high_heap = []

    all_medians = []
    median = 0

    for item in data:

        if item < median:
            heappush(low_heap, item)
        else:
            heappush(high_heap, item)

        if (len(low_heap) - len(high_heap)) > 1:
            swap_value = low_heap.pop(low_heap.index(max(low_heap)))
            heappush(high_heap, swap_value)

        if (len(low_heap) - len(high_heap)) < -1:
            swap_value = heappop(high_heap)
            heappush(low_heap, swap_value)

        len_dif = len(low_heap) - len(high_heap)

        if len(low_heap) > 0:
            low_heap_high = nlargest(1, low_heap)[0]
        else:
            low_heap_high = 0

        if len(high_heap) > 0:
            high_heap_low = nsmallest(1, high_heap)[0]
        else:
            high_heap_low = 0

        if len_dif == 0:
            median = low_heap_high
        elif len_dif == 1:
            median = low_heap_high
        else:
            median = high_heap_low

        all_medians.append(median)

    print(sum(all_medians) % 10000)


def open_problem_file(file_path):

    with open(file_path) as file:
        data = [int(x.strip()) for x in file.readlines()]

    return data


if __name__ == '__main__':
    main()
