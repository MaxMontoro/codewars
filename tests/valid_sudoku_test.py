import unittest

from katas.valid_sudoku import *


class TestValidSudoku(unittest.TestCase):
    def setUp(self):
        self.valid_sudoku = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                             [6, 7, 2, 1, 9, 5, 3, 4, 8],
                             [1, 9, 8, 3, 4, 2, 5, 6, 7],
                             [8, 5, 9, 7, 6, 1, 4, 2, 3],
                             [4, 2, 6, 8, 5, 3, 7, 9, 1],
                             [7, 1, 3, 9, 2, 4, 8, 5, 6],
                             [9, 6, 1, 5, 3, 7, 2, 8, 4],
                             [2, 8, 7, 4, 1, 9, 6, 3, 5],
                             [3, 4, 5, 2, 8, 6, 1, 7, 9]]

        self.invalid_sudoku = [  [5, 3, 4, 6, 7, 8, 9, 1, 2],
                                 [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                 [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                 [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                 [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                 [3, 0, 0, 4, 8, 1, 1, 7, 9]]

        self.invalid_sudoku_2 = [   [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                    [2, 3, 4, 5, 6, 7, 8, 9, 1],
                                    [3, 4, 5, 6, 7, 8, 9, 1, 2],
                                    [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                    [5, 6, 7, 8, 9, 1, 2, 3, 4],
                                    [6, 7, 8, 9, 1, 2, 3, 4, 5],
                                    [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                    [8, 9, 1, 2, 3, 4, 5, 6, 7],
                                    [9, 1, 2, 3, 4, 5, 6, 7, 8]]


    def test_invalid_sudoku(self):
        self.assertFalse(validSolution(self.invalid_sudoku))

    def test_invalid_sudoku_2(self):
        self.assertFalse(validSolution(self.invalid_sudoku_2))

    def test_valid_sudoku(self):
        self.assertTrue(validSolution(self.valid_sudoku))
