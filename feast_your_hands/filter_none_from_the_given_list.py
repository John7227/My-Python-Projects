def remove_none_from_the_list(numbers):

    return list(filter(None, numbers))


numbers = [1, None, 3, None, 5]

print(remove_none_from_the_list(numbers))
