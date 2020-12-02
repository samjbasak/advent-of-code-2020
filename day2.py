with open('day2.txt', 'r') as f:
    input_data = []
    for item in f:
        if item != '\n':
            password_item = item.replace('\n', '')
            min_val = password_item.split('-')
            max_val, letter_to_check, password = min_val[1].split(' ')
            input_data.append({
                'password': password,
                'num_input_1': int(min_val[0]),
                'num_input_2': int(max_val),
                'letter_to_check': letter_to_check[0]
            })

def password_valid_numbers(pw_data):
    min_val = pw_data['num_input_1']
    max_val =  pw_data['num_input_2']
    pw =  pw_data['password']
    ltc =  pw_data['letter_to_check']
    if min_val <= pw.count(ltc) <= max_val:
        return True
    else:
        return False

def password_valid_position(pw_data):
    pos_1 = pw_data['num_input_1'] - 1
    pos_2 =  pw_data['num_input_2'] - 1
    pw =  pw_data['password']
    ltc =  pw_data['letter_to_check']
    if (pw[pos_1] == ltc or pw[pos_2] == ltc) and pw[pos_1] != pw[pos_2]:
        return True
    else:
        return False

print(sum([password_valid_position(i) for i in input_data]))
