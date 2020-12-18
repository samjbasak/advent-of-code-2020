import day18_ee
import day18_ee2

with open('day18.txt') as f:
    input_data = f.read().split('\n')
    total = 0
    for i in input_data:
        if i != '':
            # Part 1
            #total += day18_ee.return_value(i)
            # Part 2
            total += day18_ee2.return_value(i)
    print(total)
