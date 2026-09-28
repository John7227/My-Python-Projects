def convert_temperatures_from_celsius_to_fahrenheit(celsius):

    return (celsius * 9/5) + 32

def get_the_result(celsius):

    return list(map(convert_temperatures_from_celsius_to_fahrenheit, celsius))

celsius = [0, 20, 37, 100]

print(get_the_result(celsius))

