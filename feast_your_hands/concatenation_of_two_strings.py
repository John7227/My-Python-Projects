from functools import reduce

def concatenation_of_two_strings(first_word, second_word):

    return first_word + second_word

def get_result(words):

    return reduce(concatenation_of_two_strings, words)


words = ["Hello", " ", "World"]

print(get_result(words))
