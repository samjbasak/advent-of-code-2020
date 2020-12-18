with open('day10.txt') as f:
    input_data = f.read().split('\n')
    input_data = [int(i) for i in input_data if i != '']
    input_data.append(0)
    input_data.append(max(input_data)+3)
    input_data.sort()

print(input_data)

incs = {1:0, 2:0, 3:0}

# Part 1
for count, i in enumerate(input_data[:-1]):
    incs[input_data[count+1] - input_data[count]] += 1

#print(incs[1] * incs[3])


# Part 2
valid_moves_backward = {i:
               [i-j for j in range(1,4) if i-j in input_data]
               for i in input_data
               }
valid_moves_backward[0] = [0]

valid_routes = {0:1}

for i in input_data[1:]:
    routes = 0
    for j in valid_moves_backward[i]:
        routes += valid_routes[j]
    valid_routes[i] = routes

print(valid_routes)

