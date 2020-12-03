import math

def read_in_file(file_name):
    with open(file_name, 'r') as f:
        data_input = []
        for item in f:
            if item != '\n':
                data_input.append(item.replace('\n', ''))
    return data_input

data_input = read_in_file('day3.txt')

def search_path(across, down, position=(0,0), trees_hit=0):
    if position[0] >= len(data_input):
        return trees_hit
    else:
        hit_tree_this_time = data_input[position[0]][position[1]] == '#'
        next_position = (
            position[0]+down,
            (position[1]+across) % len(data_input[0])
        )
        return search_path(across, down, next_position, trees_hit+hit_tree_this_time)

values = [search_path(1, 1),
          search_path(3, 1),
          search_path(5, 1),
          search_path(7, 1),
          search_path(1, 2)
          ]

print(math.prod(values))
