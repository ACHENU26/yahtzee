import unittest 
from unittest import TestCase
from yahtzee import Yahtzee

#### Upper section combinaisons tests
class test_yatzee(TestCase):
    def test_sum_1(self):
        assert Yahtzee.Turn([1, 2, 3, 4, 5], 1) == 1

    def test_sum_6(self):
        assert Yahtzee.Turn([1, 2, 6, 5, 6], 6) == 12





#### Lower section combinaisons tests

if __name__ == '__main__':
    unittest.main()