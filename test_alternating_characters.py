import unittest
from alternating_characters import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):

    def test_all_same_characters(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)

    def test_already_alternating(self):
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)

    def test_mixed_repeats(self):
        self.assertEqual(alternatingCharacters("AAABBB"), 4)

    def test_complex_repeats(self):
        self.assertEqual(alternatingCharacters("AABBAABB"), 4)

    def test_single_character(self):
        self.assertEqual(alternatingCharacters("A"), 0)