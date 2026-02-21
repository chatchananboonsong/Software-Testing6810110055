import unittest
from grid_challenge import gridChallenge

class TestGridChallenge(unittest.TestCase):

    def test_passed_grid(self):
        grid = ['abc', 'ade', 'efg']
        self.assertEqual(gridChallenge(grid), "YES")

    def test_failed_grid(self):
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        grid_no = ['zyx', 'wvu', 'tsr']
        self.assertEqual(gridChallenge(grid_no), "NO")

    def test_single_element(self):
        self.assertEqual(gridChallenge(['a']), "YES")

    def test_repeated_chars(self):
        grid = ['aaa', 'aaa', 'aaa']
        self.assertEqual(gridChallenge(grid), "YES")

    def test_complex_yes(self):
        grid = ['kc', 'iu']
        self.assertEqual(gridChallenge(grid), "YES")