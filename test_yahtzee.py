from unittest import TestCase, main, mock, main
from unittest.mock import MagicMock
from yahtzee import yahtzee


class test_mock(TestCase):
    def test_yatzy_scores_50():
        expected = 50
        actual = Yatzy.yatzy([4,4,4,4,4])
        assert expected == actual
        assert 50 == Yatzy.yatzy([6,6,6,6,6])
        assert 0 == Yatzy.yatzy([6,6,6,6,3])
    






if __name__ == '__main__':
    unittest.main()