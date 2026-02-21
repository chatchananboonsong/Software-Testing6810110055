import unittest
import staircase

class TestStaircase(unittest.TestCase):

    def test_give_4_with_hash_should_be_staircase_size_4(self):
        n = 4
        pattern = '#'
        expected_output = "   #\n  ##\n ###\n####"
        result = staircase.staircase(n, pattern)
        self.assertEqual(result, expected_output, f'Should be \n{expected_output}')

    def test_give_1_with_star_should_be_star(self):
        n = 1
        pattern = '*'
        expected_output = "*"
        result = staircase.staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_2_with_hash_should_be_staircase_size_2(self):
        n = 2
        pattern = '#'
        expected_output = " #\n##"
        result = staircase.staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_3_with_alphabet_O_should_be_staircase_size_3(self):
        n = 3
        pattern = 'O'
        expected_output = "  O\n OO\nOOO"
        result = staircase.staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_0_should_return_empty_string(self):
        n = 0
        pattern = '#'
        expected_output = ""
        result = staircase.staircase(n, pattern)
        self.assertEqual(result, expected_output)
