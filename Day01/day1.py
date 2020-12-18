from itertools import combinations
import math

def read_in_file(file_name):
    with open(file_name, 'r') as f:
        input_data = []
        for item in f:
            if item != '\n':
                yield int(item.replace('\n', ''))

input_data = read_in_file('day1.txt')

def add_up_to_2020(no_of_digits, data=input_data):
    for i in combinations(data, no_of_digits):
        if sum(i) == 2020:
            return math.prod(list(i))
            
print(add_up_to_2020(3))
