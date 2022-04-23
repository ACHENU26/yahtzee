import unittest 
from unittest import TestCase
from yahtzee import Yahtzee

class test_Yatzee(TestCase):
    
#### Upper section combinaisons tests
    def test_ones(self):
        assert Yahtzee.ones(1,2,3,4,5) == 1
        assert Yahtzee.ones(1,2,1,4,5) == 2 

    def test_twos():
        assert Yahtzee.two(1,2,3,2,6) == 4
        assert Yahtzee.two(2,2,3,2,2) == 8
    
    def test_threes():
        assert Yahtzee.three(1,2,3,2,3) == 6
        assert Yahtzee.three(1,2,3,3,3) == 9
    
    def test_fours():
        assert Yahtzee(4,5,4,5,6).four() == 8
        assert Yahtzee(4,4,4,5,6).four() == 12
    
    def test_fives():
        assert Yahtzee(2,3,4,5,5).five() == 10
        assert Yahtzee(3,4,5,5,5).five() == 15
    
    def test_sixes():
        assert Yahtzee(4,4,6,5,6).sixe() == 12
        assert Yahtzee(4,6,6,5,6).sixe() == 18

#### Lower section combinaisons tests











if __name__ == '__main__':
    unittest.main()