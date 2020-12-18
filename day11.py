with open('day11.txt') as f:
    input_data = f.read().split('\n')
    input_data = [list(i) for i in input_data if i != '']

'''
input_data[0][0] = '#'
input_data[0][1] = '#'
input_data[1][0] = '#'
input_data[2][2] = '#'
'''

def create_empty_seating_chart(seat_pattern):
    new_pattern = []
    for row in seat_pattern:
        new_row = []
        for seat in row:
            if seat == '.':
               new_row.append('.')
            else:
                new_row.append('')
        new_pattern.append(new_row)
    return new_pattern

def find_adjacent_seats(seat, seat_pattern=input_data):
    r, c = seat
    adjacent_seats = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if r+i >= 0 and r+i < len(seat_pattern) and c+j >= 0 and c+j < len(seat_pattern[0]):
                adjacent_seats.append((r+i, c+j))
    adjacent_seats.remove(seat)
    return adjacent_seats

def count_adjacent_occupied_seats(seat, seat_pattern=input_data):
    adjacent_seats = find_adjacent_seats(seat)
    return sum([seat_pattern[i][j] == '#' for i,j in adjacent_seats])

def next_seat_state(seat, seat_pattern=input_data):
    adjacent_seats = count_adjacent_occupied_seats(seat, seat_pattern)
    if seat_pattern[seat[0]][seat[1]] == 'L' and adjacent_seats == 0:
        return '#', True
    if seat_pattern[seat[0]][seat[1]] == '#' and adjacent_seats >= 4:
        return 'L', True
    return seat_pattern[seat[0]][seat[1]], False


def next_iteration(seat_pattern):
    change_ind = False
    new_seating_pattern = create_empty_seating_chart(seat_pattern)
    for row_num, row in enumerate(seat_pattern):
        for seat_num, seat in enumerate(row):
            new_seating_pattern[row_num][seat_num], change = next_seat_state((row_num, seat_num), seat_pattern)
            change_ind = change_ind or change
    return new_seating_pattern, change_ind


# Part 1
'''
change_ind = True
seat_pattern = input_data
while change_ind:
#for j in range(2):
    seat_pattern, change_ind = next_iteration(seat_pattern)
    #for i in seat_pattern:
    #    print(''.join(i))
    #print()


count = 0
#for i in range(len(seat_pattern)):
#    for j in range(len(seat_pattern[i])):
#        if seat_pattern[i][j] == '#':
#            count += 1

print(count)
'''
# Part 2

vectors = [(-1, -1), (-1, 0), (-1, 1),
           (1, -1), (1, 0), (1, 1),
           (0, -1), (0, 1)
          ]
#print(vectors)

def check_if_seat_out_of_range(seat, seat_pattern=input_data):
    if seat[0] < 0 or seat[0] >= len(seat_pattern):
        return False
    if seat[1] < 0 or seat[1] >= len(seat_pattern[0]):
        return False
    else:
        return True
    

def find_vector_adjacent_seats(seat, vector, seat_pattern):
    while True:
        new_seat = seat[0]+vector[0], seat[1]+vector[1]
        if not check_if_seat_out_of_range(new_seat, seat_pattern):
            return 0
        if seat_pattern[new_seat[0]][new_seat[1]] == 'L':
            return 0
        if seat_pattern[new_seat[0]][new_seat[1]] == '#':
            return 1
        seat = new_seat


def count_adjacent_occupied_seats_vectors(seat, seat_pattern=input_data):
    adjacent_seats = vectors
    return sum([
                find_vector_adjacent_seats(
                    seat,
                    i,
                    seat_pattern
                    )
                for i in adjacent_seats])


def next_seat_state_vectors(seat, seat_pattern=input_data):
    adjacent_seats = count_adjacent_occupied_seats_vectors(seat, seat_pattern)
    if seat_pattern[seat[0]][seat[1]] == 'L' and adjacent_seats == 0:
        return '#', True
    if seat_pattern[seat[0]][seat[1]] == '#' and adjacent_seats >= 5:
        return 'L', True
    return seat_pattern[seat[0]][seat[1]], False


def next_iteration_vectors(seat_pattern):
    change_ind = False
    new_seating_pattern = create_empty_seating_chart(seat_pattern)
    for row_num, row in enumerate(seat_pattern):
        for seat_num, seat in enumerate(row):
            new_seating_pattern[row_num][seat_num], change = next_seat_state_vectors((row_num, seat_num), seat_pattern)
            change_ind = change_ind or change
    return new_seating_pattern, change_ind

change_ind = True
seat_pattern = input_data
while change_ind:
    for j in range(2):
        seat_pattern, change_ind = next_iteration_vectors(seat_pattern)
        for i in seat_pattern:
            print(''.join(i))
        print()


count = 0
for i in range(len(seat_pattern)):
    for j in range(len(seat_pattern[i])):
        if seat_pattern[i][j] == '#':
            count += 1

print(count)
