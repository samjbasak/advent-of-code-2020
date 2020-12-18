def read_in_file(file_name):
    with open(file_name, 'r') as f:
        input_data = []
        for item in f:
            if item != '\n':
                input_data.append(item.replace('\n', ''))
    return input_data


input_data = read_in_file('day5.txt')


def range_reducer(
                seat_code,
                row_range,
                top_half=['B', 'R'],
                bottom_half=['F', 'L']
                ):
    for code in seat_code:
        if code in top_half:
           row_range = (
                int(row_range[0]+(row_range[1]-row_range[0]+1)/2),
                row_range[1]) 
        elif code in bottom_half:
            row_range = (
                row_range[0],
                int(row_range[1]-(row_range[1]-row_range[0]+1)/2))
    if row_range[0] == row_range[1]:
        return row_range[0]
    else:
       raise ValueError('Not limited to one seat')


def seat_checker(seat_code):
    row = range_reducer(seat_code[:7], (0, 127))
    column = range_reducer(seat_code[7:], (0, 7))
    return row, column


def calculate_seat_id(seat_code):
    seat_nums = seat_checker(seat_code)
    return seat_nums[0] * 8 + seat_nums[1]


def highest_seat_id(seats):
    highest_seat_id = 0
    for seat_code in input_data:
        seat_id = calculate_seat_id(seat_code)
        highest_seat_id = max(highest_seat_id, seat_id)
    return highest_seat_id


def find_missing_seat_ids(seats):
    possible_seats = list(range(highest_seat_id(input_data)+1))
    for seat_code in seats:
        seat_id = calculate_seat_id(seat_code)
        possible_seats.remove(seat_id)
    return possible_seats


print(find_missing_seat_ids(input_data))
