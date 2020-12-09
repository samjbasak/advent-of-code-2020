from itertools import combinations


with open('day9.txt') as f:
    input_data = f.read().split('\n')
    input_data = [int(i) for i in input_data if i != '']


def valid_number(target, options):
    for i in combinations(options, 2):
        if sum(i) == target:
            return True
    return False


def find_invalid_number(input_data, preamble):
    for count, target in enumerate(input_data[preamble:]):
        if not valid_number(target, input_data[count:count+preamble]):
            return target

def find_contiguous_numbers(target):
    for count, i in enumerate(input_data):
        total, next = i, 1
        while total <= target:
            if total == target:
                return min(input_data[count:count+next]) + max(input_data[count:count+next])
            total += input_data[count+next]
            next += 1
             

target = find_invalid_number(input_data, 25)
print(find_contiguous_numbers(target))
