def format_a_line(line):
    bag_rule, rules = line.split(' contain ')
    return bag_rule, rules.split(', ')

with open('day7.txt') as f:
    input_data = f.read().replace('\n', '').replace(' bags', '').replace(' bag', '')[:-1].split('.')
    data = {
        format_a_line(idx)[0]: format_a_line(idx)[1]
        for idx in input_data
    }
    for i in data:
        if data[i] == ['no other']:
            data[i] = {}
        else:
            data[i] = {j[2:]:j[0] for j in data[i]}



def look_up_colours(bag_to_check, shiny_gold_ind=0):
    for bag in data[bag_to_check]:
        if bag == 'shiny gold':
            return 1
        elif data[bag]:
            shiny_gold_ind = max(look_up_colours(bag, shiny_gold_ind), shiny_gold_ind)
    return shiny_gold_ind


# Part 1
print(sum([1 for i in data if look_up_colours(i)]))

#print(data)

# Part 2
def find_total_number_of_bags(bag_to_check):
    total_bags = 1
    if data[bag_to_check]:
        for bag in data[bag_to_check]:
            bags_required = int(data[bag_to_check][bag])
            total_bags += bags_required * find_total_number_of_bags(bag)
    return total_bags
        


print(find_total_number_of_bags('shiny gold'))
