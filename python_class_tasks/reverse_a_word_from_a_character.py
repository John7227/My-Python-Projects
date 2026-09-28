def reverse_a_word_from_a_character(word):

    first = "";
    second = "";

#    character = 'd'

    first = word[-5: -9:-1]

    second = word[-1:-6:-1]

    return first + second

word = "abcdefgh";

print(reverse_a_word_from_a_character(word))
