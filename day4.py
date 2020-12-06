from functools import partial

def read_in_file(file_name):
    with open(file_name, 'r') as f:
        input_data = []
        passport = {}
        for line in f:
            if line == '\n':
                input_data.append(passport)
                passport = {}
            else:
                fields = line.split(' ')
                for item in fields:
                    field, value = item.split(':')
                    passport[field] = value.replace('\n', '')
    return input_data


input_data = read_in_file('day4.txt')


def value_between(min_val, max_val, act_val):
    return min_val <= int(act_val) <= max_val


def value_between_units(units, min_val, max_val, act_val):
    unit = [unit for unit in units if unit in act_val]
    if not any(unit):
        return False
    if unit[0] in act_val:
        val = int(act_val.replace(unit[0], ''))
        return min_val[unit[0]] <= val <= max_val[unit[0]]


def position_value(positions, act_val):
    for pg in positions:
        for position in range(pg[0], pg[1]+1):
            if len(act_val) > pg[1] and act_val[position] not in positions[pg]:
                return False
    return True


def value(poss_vals, act_val):
    return act_val in poss_vals


def length(min_len, max_len, act_val):
    return min_len <= len(act_val) <= max_len


fields = {
    'byr': [partial(value_between, 1920, 2002)],
    'iyr': [partial(value_between, 2010, 2020)],
    'eyr': [partial(value_between, 2020, 2030)],
    'hgt': [partial(value_between_units,
                   ['cm', 'in'],
                   {'cm': 150, 'in': 59},
                   {'cm': 193, 'in': 76}
                   )
           ],
    'hcl': [partial(position_value,
                   {(0,0): '#', (1,6): '1234567890abcdef',}
                   ),
            partial(length, 7, 7),
           ],
    'ecl': [partial(value, ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),],
    'pid': [partial(position_value,
                   {(0,8): '1234567890'},
                   ),
            partial(length, 9, 9),
           ],
    'cid': []
}


def passport_check(passport, fields, mandatory_fields):
    for field in fields:
        if field not in passport and field in mandatory_fields:
            return False
        if not all([func(passport[field]) for func in fields[field]]):
            return False
    return True

counter = 0
for passport in input_data:
    if passport_check(passport, fields, ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
        counter += 1

print(counter)
