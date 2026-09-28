from functools import reduce

def find_the_maximum_value_in_the_list(number, numbers):

    if number > numbers:
        return number

    else:
        return numbers

def get_result(numbers):

    return reduce(find_the_maximum_value_in_the_list, numbers)

numbers = [3, 7, 2, 9, 1]

print(get_result(numbers))
