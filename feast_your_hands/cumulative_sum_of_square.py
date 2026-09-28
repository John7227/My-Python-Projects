from functools import reduce

def cumulative_sum_of_square(number, numbers):

    return number + (numbers**2)

def get_result(numbers):
    
    return reduce(cumulative_sum_of_square, numbers)


numbers = [1, 2, 3]

print(get_result(numbers))
