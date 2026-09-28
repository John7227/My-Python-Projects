import unittest 

from palindrome import *

class PalindromeTest(unittest.TestCase):

    def test_that_I_input_a_list_of_strings_and_it_returns_true_if_each_String_are_palindrome(self):

        words = ["Madam", "hello", "noon", "racecar"];

        expected = [True, False, True, True];

        actual = palindrome(words)

        self.assertListEqual(expected, actual)


