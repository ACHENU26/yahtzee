import unittest 
from unittest import TestCase
from yahtzee import Yahtzee


class test_yatzee(TestCase):
    def test_sum_1(self):
        assert Yahtzee.Turn([1, 2, 3, 4, 5], 1) == 1

    def test_sum_6(self):
        assert Yahtzee.Turn([1, 2, 6, 5, 6], 6) == 12

    def test_sum_Invalid(self):
        assert Yahtzee.Turn([1, 2, 6, 5, 6], 3) == 0




if __name__ == '__main__':
    unittest.main()