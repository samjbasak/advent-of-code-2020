with open('day12.txt') as f:
    input_data = f.read().split('\n')
    input_data = [(i[0], int(i[1:])) for i in input_data if i != '']

print(input_data)

directions = {'N': (0, 1),
              'S': (0, -1),
              'E': (1, 0),
              'W': (-1, 0),
             }

rotations = {
             'R': 1,
             'L': -1
             }

ninety_degree = {'N': {'R': 'E', 'L': 'W'},
                 'S': {'R': 'W', 'L': 'E'},
                 'E': {'R': 'S', 'L': 'N'},
                 'W': {'R': 'N', 'L': 'S'},
                 }

def add_on_vector(place, direction, steps):
    return (
            place[0] + (direction[0] * steps),
            place[1] + (direction[1] * steps)
            )


def rotate(direction, rotation_direction, rotation_degrees):
    no_rotations = int(rotation_degrees / 90)
    x, y = direction
    for i in range(no_rotations):
        x,y = (y * rotations[rotation_direction], -x * rotations[rotation_direction])
    return x,y


# Part 1
'''
place = (0,0)
direction = (1, 0)

for i in input_data:
    print(place, direction)
    if i[0] in ['R', 'L']:
        direction = rotate(direction, i[0], i[1])
    elif i[0] == 'F':
        place = add_on_vector(place, direction, i[1])
    elif i[0] in ['N', 'S', 'E', 'W']:
        place = add_on_vector(place, directions[i[0]], i[1])

print(place)
'''

# Part 2

place = (0,0)
waypoint = (10,1)

for i in input_data:
    print(place, waypoint, i)
    if i[0] in ['R', 'L']:
        waypoint = rotate(waypoint, i[0], i[1])
    elif i[0] == 'F':
        place = add_on_vector(place, waypoint, i[1])
    elif i[0] in ['N', 'S', 'E', 'W']:
        waypoint = add_on_vector(waypoint, directions[i[0]], i[1])

print(place, waypoint)
