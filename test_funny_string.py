import unittest
from funny_string import funnyString

class TestFunnyString(unittest.TestCase):
    def test_example_1_funny(self):
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_example_2_not_funny(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_repeated_chars_funny(self):
        self.assertEqual(funnyString("aaaaa"), "Funny")

    def test_minimum_length_funny(self):
        self.assertEqual(funnyString("ab"), "Funny")

    def test_high_ascii_diff_not_funny(self):
        self.assertEqual(funnyString("azyx"), "Not Funny")