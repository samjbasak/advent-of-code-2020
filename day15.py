input_data = [1,17,0,10,18,11,6]

last_position = {i:input_data.index(i) for i in input_data}
print(last_position)


def next_number(sequence):
    last_place = len(sequence) - 1
    if sequence[-1] in last_position:
        previous_place = last_position[sequence[-1]]
        next_num = last_place - previous_place
    else:
        next_num = 0
    last_position[sequence[-1]] = last_place
    return next_num

sequence = input_data.copy()

for i in range(30000000-len(input_data)):
    sequence.append(next_number(sequence))

print(sequence[-10:])
