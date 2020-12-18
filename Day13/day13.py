from functools import reduce

with open('day13.txt') as f:
    input_data = f.read().split('\n')
    times = int(input_data[0])
    buses = set(int(i) for i in input_data[1].split(',') if i != '' and i != 'x')
    bus_times = [int(i) if i != 'x' else i for i in input_data[1].split(',') if i != '']

bus_positions = {int(i): bus_times.index(i) for i in bus_times if i != 'x'}

print(bus_positions)


# Part 1

nearest_bus = (0, 1000)

for bus_id in buses:
    if bus_id - (times % bus_id) < nearest_bus[1]:
        nearest_bus = (bus_id, bus_id - (times % bus_id))

print(nearest_bus[0] * nearest_bus[1])


#https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

offsets = [-bus_times.index(bus) for bus in buses]
print("Part 2:")
print(chinese_remainder(buses, offsets))
