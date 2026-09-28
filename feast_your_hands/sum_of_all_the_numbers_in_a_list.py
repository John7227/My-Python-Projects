from functools import reduce

def sum_up(number, numbers):

    return number + numbers

def get_result(numbers):

    return reduce(sum_up, numbers)



numbers = [1, 2, 3, 4, 5]

print(get_result(numbers))



