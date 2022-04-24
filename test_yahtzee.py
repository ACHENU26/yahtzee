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

    def test_ThreeOfAKind_valid(self):
        assert Yahtzee.turn([1, 1, 1, 5, 6], "threeOfAKind") == 14

    def test_ThreeOfAKind_invalid(self):
        assert Yahtzee.turn([1, 1, 4, 5, 6], "threeOfAKind") == 0

    def test_FourOfAKind_valid(self):
        assert Yahtzee.turn([1, 2, 2, 2, 2], "fourOfAKind") == 9

    def test_FourOfAKind_invalid(self):
        assert Yahtzee.turn([1, 4, 2, 2, 2], "fourOfAKind") == 0

    def test_FullHouse_valid(self):
        assert Yahtzee.turn([5, 5, 5, 1, 1], "fullHouse") == 25

    def test_FullHouse_invalid(self):
        assert Yahtzee.turn([1, 2, 4, 4, 4], "fullHouse") == 0

    def test_SmallStraight_valid(self):
        assert Yahtzee.turn([6, 2, 3, 4, 1], "smallStraight") == 30

    def test_SmallStraight_invalid(self):
        assert Yahtzee.turn([1, 2, 4, 5, 5], "smallStraight") == 0

    def test_LargeStraight_valid(self):
        assert Yahtzee.turn([2, 5, 4, 3, 6], "largeStraight") == 40

    def test_LargeStraight_invalid(self):
        assert Yahtzee.turn([1, 3, 4, 5, 6], "largeStraight") == 0

if __name__ == '__main__':
    unittest.main()