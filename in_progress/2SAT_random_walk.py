import random

# could set up a dictionary with true or false flags for each sat tp
# can then iterate through tps and keep flipping till all are true

problem_path = '../problem_files/toy2sat.txt'


def main():

    var_count, data = read_input(problem_path)

    solution = [False for x in data]
    sat = {x: False for x in data}

    for s in sat:
        if True:
            pass

    for i in range(var_count):

        for k, v in sat.items():

            if True:
                pass


def read_input(path):

    with open(path) as file:
        var_count = int(file.readline())
        data = [tuple(int(i) - 1 for i in x.split()) for x in file.readlines()]

    return var_count, data


if __name__ == '__main__':
    main()
