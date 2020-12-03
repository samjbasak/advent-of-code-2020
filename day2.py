def read_in_file(file_name):
    with open(file_name, 'r') as f:
        for item in f:
            if item != '\n':
                password_item = item.replace('\n', '')
                min_val = password_item.split('-')
                max_val, letter_to_check, password = min_val[1].split(' ')
                yield {
                    'pw': password,
                    'num_input_1': int(min_val[0]),
                    'num_input_2': int(max_val),
                    'ltc': letter_to_check[0]
                }

input_data = read_in_file('day2.txt')

def password_valid_numbers(pw_data):
    min_val = pw_data['num_input_1']
    max_val =  pw_data['num_input_2']
    return min_val <= pw_data['pw'].count(pw_data['ltc']) <= max_val

def password_valid_position(pw_data):
    pos_1 = pw_data['num_input_1'] - 1
    pos_2 =  pw_data['num_input_2'] - 1
    return ((pw_data['pw'][pos_1] == pw_data['ltc'])
            ^
            (pw_data['pw'][pos_2] == pw_data['ltc'])
            )

print(sum(password_valid_position(i) for i in input_data))
