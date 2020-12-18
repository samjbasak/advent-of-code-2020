from itertools import product

with open('day14.txt') as f:
    input_data = f.read().split('mask = ')
    input_data = [i[:-1].split('\n') for i in input_data if i != '']
    sorted_data = []
    for position, part in enumerate(input_data):
        sorted_data.append((part[0], []))
        for command in part[1:]:
            if command != '':
                sorted_data[position][1].append((int(command[command.find('[')+1:command.find(']')]), int(command[command.find(' = ')+3:])))

#print(input_data)
print(sorted_data)

memory_addresses = {}

def calculate_number(mask, value):
    num = format(value, '036b')
    new_num = ''
    for i in range(len(num)):
        if mask[i] != 'X':
            new_num += mask[i]
        else:
            new_num += num[i]
    return new_num

'''
# Part 1
for mask in sorted_data:
    for i in mask[1]:
        memory_addresses[i[0]] = calculate_number(mask[0], i[1])

total = 0
for i in memory_addresses:
    total += int(memory_addresses[i], 2)

print(total)

#print(memory_addresses)
'''

def calculate_number_range(mask, value):
    num = format(value, '036b')
    values = []
    combinations = product(range(2), repeat=mask.count('X'))
    for choices in combinations:
        new_num = ''
        choice = 0
        for i in range(len(num)):
            if mask[i] == 'X':
                new_num += str(choices[choice])
                choice += 1
            elif mask[i] == '1':
                new_num += '1'
            else:
                new_num += num[i]
        values.append(new_num)
    return values


for mask in sorted_data:
    for i in mask[1]:
        current_mem_adds = calculate_number_range(mask[0], i[0])
        for j in current_mem_adds:
            memory_addresses[j] = i[1]


for i in memory_addresses:
    print(int(i,2), memory_addresses[i])

total = 0
for i in memory_addresses:
    print(memory_addresses[i])
    total += int(memory_addresses[i])

print(total)

