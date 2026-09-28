from functools import reduce

def find_the_product_of_all_numbers(number, numbers):

    return number * numbers

def get_result(numbers):

    return reduce(find_the_product_of_all_numbers, numbers)



numbers = [2, 3, 4]

print(get_result(numbers))
