from itertools import combinations
import math

with open('day1.txt', 'r') as f:
    input_data = []
    for item in f:
        if item != '\n':
            input_data.append(int(item.replace('\n', '')))


def add_up_to_2020(no_of_digits, data=input_data):
    combs = combinations(data, no_of_digits)
    for i in combs:
        if sum(i) == 2020:
            return math.prod(list(i))
            
print(add_up_to_2020(5))
