from functools import reduce

def merge_a_list_of_dictionaries_into_a_single_dictionary(number, numbers):

    return number | numbers

def get_result(numbers):

    return reduce(merge_a_list_of_dictionaries_into_a_single_dictionary, numbers)
    


numbers = [{'a': 1}, {'a': 2}, {'a': 3}]

print(get_result(numbers))


