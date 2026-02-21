import unittest
from two_characters import alternate

class TestTwoCharacters(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(alternate("beabeefeab"), 5)

    def test_no_valid_string(self):
        self.assertEqual(alternate("aaaaa"), 0)

    def test_already_valid(self):
        self.assertEqual(alternate("ababab"), 6)

    def test_too_short(self):
        self.assertEqual(alternate("a"), 0)

    def test_multiple_possibilities(self):
        self.assertEqual(alternate("abacaba"), 3)