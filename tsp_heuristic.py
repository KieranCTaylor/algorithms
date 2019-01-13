import math
from collections import namedtuple
import sys
import copy


City = namedtuple('City', ['index', 'coordinates'])

problem_path = 'problem_files/nn.txt'


def main():
    """
    Use a heuristic to calculate an approximate solution to the travelling salesman problem
    """

    result = iterate_cities(open_input(problem_path))

    print(result)


def iterate_cities(cities):

    current_city = cities.pop(0)
    distances = []

    first_city = copy.deepcopy(current_city)

    while len(cities) > 0:

        current_city, next_distance = tsp_heuristic(current_city, cities)
        cities.pop(cities.index(current_city))
        distances.append(next_distance)

    final_distance = euclid_distance(current_city.coordinates, first_city.coordinates)
    distances.append(final_distance)

    return sum(distances)


def euclid_distance(p1, p2):

    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def tsp_heuristic(current_city, cities):

    min_distance = sys.maxsize
    min_city = None

    for city in cities:

        distance_to_current = euclid_distance(current_city.coordinates, city.coordinates)
        if distance_to_current < min_distance:
            min_distance = distance_to_current
            min_city = city

    return min_city, min_distance


def open_input(path):

    with open(path) as file:
        header = file.readline()
        data = [x.split() for x in file.readlines()]

    cities = []

    for line in data:
        new_city = City(int(line[0]), (float(line[1]), float(line[2])))
        cities.append(new_city)

    print('Input read!')

    return cities


if __name__ == '__main__':

    main()
