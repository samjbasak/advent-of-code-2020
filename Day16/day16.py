def tidy_fields(input_data):
    input_data = input_data.split('\n')
    data = {}
    for i in input_data:
        place = i.find(':')
        ranges = i[place+2:]
        ranges = ranges.split(' or ')
        ranges = [j.split('-') for j in ranges]
        data[i[:place]] = ranges
    return data

def tidy_your_ticket(input_data):
    index = input_data.find('\n')
    return input_data[index+1:].split(',')

def tidy_nearby_tickets(input_data):
    return [i.split(',') for i in input_data[16:-1].split('\n')]

with open('day16.txt') as f:
    input_data = f.read().split('\n\n')
    #print(input_data)

fields = tidy_fields(input_data[0])
your_ticket = tidy_your_ticket(input_data[1])
nearby_tickets = tidy_nearby_tickets(input_data[2])


def check_if_data_in_range(fields, nearby_ticket):
    invalid_values = []
    for value in nearby_ticket:
        in_range = False
        for field in fields:
            for inner_field in fields[field]:
                if int(value) in range(int(inner_field[0]), int(inner_field[1])+1):
                    in_range = True
        if not in_range:
            invalid_values.append(int(value))
    return invalid_values


invalid_tickets = [check_if_data_in_range(fields, i) for i in nearby_tickets]

total = 0
for i in invalid_tickets:
    total += sum(i)
print(total)




def check_value_in_field_range(value, field):
    for field_range in field:
        if int(value) in range(int(field_range[0]), int(field_range[1])+1):
            return True
    return False


def possible_valid_fields(fields, your_ticket):
    positions = []
    for value in your_ticket:
        possible_fields = []
        for field in fields:
            if check_value_in_field_range(value, fields[field]):
                possible_fields.append(field)
        positions.append(possible_fields)
    return positions

#print()
valid_tickets = [i for i in nearby_tickets if not check_if_data_in_range(fields, i)]
possible_fields = possible_valid_fields(fields, your_ticket)
actual_field = []
for idx in range(len(your_ticket)):
    possible_actual_fields = []
    for field in possible_fields[idx]:
        valid_field = True   
        for ticket in valid_tickets:
            if not check_value_in_field_range(ticket[idx], fields[field]):
                valid_field = False
                pass
        if valid_field:
            possible_actual_fields.append(field)
    actual_field.append(possible_actual_fields)


changed = 1


while changed:
    changed = 0
    for field in actual_field:
        if len(field) == 1:
            for item in field:
                right_field = item
            for field2 in actual_field:
                if right_field in field2 and len(field2) != 1:
                    field2.remove(right_field)
        else:
            changed += 1

total = 1
print(your_ticket)
print(actual_field)
for i in range(len(actual_field)):
    if actual_field[i][0][:9] == 'departure':
        print(i)
        total *= int(your_ticket[i])

print(total)
