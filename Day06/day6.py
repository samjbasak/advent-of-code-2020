import string

with open('day6.txt') as f:
    input_data = f.read().split('\n\n')

# Part 1
print(sum([
          len(set(idx.replace('\n', '')))
          for idx in input_data
          ]))


def intersection_of_strings(list_of_strings, initial_string=string.ascii_lowercase):
    intersected_strings = set(initial_string).intersection(list_of_strings[0])
    if len(list_of_strings) == 1:
        return intersected_strings
    return intersection_of_strings(list_of_strings[1:], intersected_strings)

# Part 2
print(sum([
           len(intersection_of_strings(idx.split()))
           for idx in input_data
           ]))
