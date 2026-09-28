import unittest

from perfect_square import *

class PerfectSquareTest(unittest.TestCase):

    def test_that_a_perfect_number_returns_true(self):

        numbers = [4, 9, 25, 49]
    
        expected = [True, True, True, True]

        actual = perfect_square(numbers)

        self.assertListEqual(expected, actual)


    def test_some_numbers_that_are_not_perfect_square_if_it_will_return_false(self):

        numbers = [8, 36, 49, 5]
    
        expected = [False, True, True, False]

        actual = perfect_square(numbers)

        self.assertListEqual(expected, actual)


