with open('day8.txt') as f:
    input_data = f.read().split('\n')
    input_data = [
                  (idx[:3], idx[4], int(idx[5:]), 0)
                  for idx in input_data
                  if idx != ''
                  ]

#print(input_data)

INSTRUCTION = 0
OPERATOR = 1
AMOUNT = 2
SEEN_YET = 3

def apply_operator(operator, value):
    if operator == '+':
        return value
    else:
        return -value

def clean_data(data):
    for i in data:
        data[position] = (data[0], data[1], data[2], 0)
    return data
    

def run_code(data):
    acc = 0
    pos = 0
    fin = False
    while True:
        if pos == len(data):
            fin = True
            break
        pos_data = data[pos]
        if pos_data[SEEN_YET] == 1:
            break
        data[pos] = (pos_data[0], pos_data[1], pos_data[2], 1)
        if pos_data[INSTRUCTION] == 'acc':
            acc += apply_operator(pos_data[OPERATOR], pos_data[AMOUNT])
            pos += 1
        elif pos_data[INSTRUCTION] == 'nop':
            pos += 1
        else:
            pos += apply_operator(pos_data[OPERATOR], pos_data[AMOUNT])
    return pos, acc, fin

#print(run_code(input_data))

for i in range(len(input_data)):
    data = list(input_data)
    pos, acc, fin = 0, 0, False
    if data[i][INSTRUCTION] == 'jmp':
        data[i] = ('nop', data[i][1], data[i][2], 0)
        pos, acc, fin = run_code(data)
    elif data[i][INSTRUCTION] == 'nop':
        data[i] = ('jmp', data[i][1], data[i][2], 0)
        pos, acc, fin = run_code(data)
    if fin:
        print(acc)
        break
