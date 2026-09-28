def add_10_to_each_elements(numbers):

    return numbers + 10


def get_the_result(numbers):

    return list(map(add_10_to_each_elements, numbers))


numbers = [0, 5, 10, 15]

print(get_the_result(numbers))
