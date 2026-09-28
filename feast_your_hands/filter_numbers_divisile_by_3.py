def extract_numbers_divisile_by_3(numbers):

    return numbers % 3 != 0


def get_result(numbers):

    return list(filter(extract_numbers_divisile_by_3, numbers))



numbers = [1, 3, 4, 6, 9, 12]

print(get_result(numbers))
