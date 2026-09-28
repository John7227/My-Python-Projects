import unittest

from perfect_square import *

class PerfectSquareTest(unittest.TestCase):

    def test_that_the_given_list_returns_True_for_the_perfect_sqaure(self):

        numbers = [0, 1, 2, 3, 4, 9, 10, 16, 25, 26]
    
        expected = [True, True, False, False, True, True, False, True, True, False]

        actual = perfect_square(numbers)

        self.assertListEqual(expected, actual)

        numbers = [0, 13, 25, 1, 4]

        expected = [True, False, False, True, True]

        actual = perfect_square(numbers)

        self.assertListEqual(expected, actual)
