problem_path = 'problem_files/2Sum.txt'

with open(problem_path) as data_file:
    data = {int(x.strip()) for x in data_file.readlines()}

counter = 0

for target in range(-10000, 10001):

    for element in data:

        if (target - element) in data:
            if element * 2 != target:
                counter += 1
                break

print(counter)
