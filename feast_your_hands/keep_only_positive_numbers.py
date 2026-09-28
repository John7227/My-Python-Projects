def remove_negative_numbers(numbers):

    return numbers >= 0

def get_result(numbers):

    return list(filter(remove_negative_numbers, numbers))


numbers = [-2, -1, 0, 1, 2]

print(get_result(numbers))
