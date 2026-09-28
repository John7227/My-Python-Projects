def perfect_square(numbers):
    square = []

    for number in numbers:
    
        result = False

        for count in range(len(numbers)):

            if count * count == number:
                result = True
                break

        square.append(result)

    return square


