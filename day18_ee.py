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


def do_sum(sum_list):
    if len(sum_list) == 1:
        return sum_list[0]
    elif sum_list[-2] == '+':
        return do_sum(sum_list[:-2]) + sum_list[-1]
    elif sum_list[-2] == '*':
        return do_sum(sum_list[:-2]) * sum_list[-1]

def deal_with_nested_lists(sum_list):
    for count, i in enumerate(sum_list):
        if isinstance(i, list):
            sum_list[count] = deal_with_nested_lists(i)
    return do_sum(sum_list)
            

def return_value(sum_string):
    my_sum = tidy_up_sum(sum_string)
    my_sum = sort_brackets(my_sum)
    return deal_with_nested_lists(my_sum)
