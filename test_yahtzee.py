import unittest 
from unittest import TestCase
from yahtzee import Yahtzee


class test_yatzee(TestCase):
    def test_sum_1(self):
        assert Yahtzee.turn([1, 2, 3, 4, 5], 1) == 1

    def test_sum_6(self):
        assert Yahtzee.turn([1, 2, 6, 5, 6], 6) == 12

    def test_sum_Invalid(self):
        assert Yahtzee.turn([1, 2, 6, 5, 6], 3) == 0

    def test_chance(self):
        assert Yahtzee.turn([1, 2, 4, 4, 6], "chance") == 17

    def test_yahtzee_valid(self):
        assert Yahtzee.turn([1, 1, 1, 1, 1], "yahtzee") == 50

    def test_yahtzee_invalid(self):
        assert Yahtzee.turn([1, 4, 4, 4, 4], "yahtzee") == 0

if __name__ == '__main__':
    unittest.main()