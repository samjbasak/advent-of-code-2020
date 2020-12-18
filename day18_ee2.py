import string
import time

OPERATORS = ['+', '*']

def find_matching_bracket(sum_string, open_p_index):
    open_ps = 0
    close_ps = 0
    for count, i in enumerate(sum_string):
        if i == ')' and open_ps == close_ps:
            return open_p_index + count + 1
        elif i == '(':
            open_ps += 1
        elif i == ')':
            close_ps += 1

    '''
    open_brackets = 
    close_p = sum_string.index(')')
    if count('(') == 0:
        return close_p + open_p_index
    else:
        find_index_next_bracket(sum_string[close_p+1:], open_p_index+close_p)
    '''
#print(find_matching_bracket('())', 0))

def tidy_up_sum(string_sum):
    sum_list = []
    for i in string_sum:
        if not sum_list:
            sum_list.append(i)
        else:
            if sum_list[-1] in string.digits and i in string.digits:
                sum_list[-1] += i
            elif i != ' ':
                sum_list.append(i)
    return [int(i) if i[0] in string.digits else i for i in sum_list]


def sort_brackets(sum_list):
    if '(' not in sum_list:
        return sum_list
    else:
        open_p = len(sum_list) - sum_list[::-1].index('(')-1
        close_p = open_p + sum_list[open_p:].index(')')
        return sort_brackets(
                sum_list[:open_p] + 
                [sum_list[open_p+1:close_p]] + 
                sum_list[close_p+1:]
               )


def make_list_into_length_three(sum_list):
    if len(sum_list) < 3:
        return [sum_list[0]] + ['+', 0]
    elif len(sum_list) == 3:
        return sum_list
    elif '+' in sum_list:
        operator = sum_list.index('+')
        sum_list = sum_list[:operator-1] + [sum_list[operator-1:operator+2]] + sum_list[operator+2:]
        return make_list_into_length_three(sum_list)
    elif '*' in sum_list:
        operator = sum_list.index('*')
        sum_list = sum_list[:operator-1] + [sum_list[operator-1:operator+2]] + sum_list[operator+2:]
        return make_list_into_length_three(sum_list)

def deal_with_nested_lists(sum_list):
    for count, i in enumerate(sum_list):
        if isinstance(i, list):
            sum_list[count] = deal_with_nested_lists(i)
    return make_list_into_length_three(sum_list)
            

def eval_list(input_list):
    left, operator, right = input_list
    return eval_individual(left, operator, right)


def eval_individual(left, operator, right):
    if isinstance(left, list) == False and isinstance(right, list) == False:
        if operator == '*':
            return left * right
        elif operator == '+':
            return left + right
    elif isinstance(left, list) == False:
        return eval_individual(left, operator, eval_list(right))
    elif isinstance(right, list) == False:
        return eval_individual(eval_list(left), operator, right)
    else:
        return eval_individual(eval_list(left), operator, eval_list(right))


def return_value(sum_string):
    my_sum = tidy_up_sum(sum_string)
    my_sum = sort_brackets(my_sum)
    my_sum = deal_with_nested_lists(my_sum)
    my_sum = make_list_into_length_three(my_sum)	
    return eval_list(my_sum)
    
print(return_value('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))





