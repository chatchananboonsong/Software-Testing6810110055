import unittest
from caesar_cipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):

    def test_standard_case(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwba")

    def test_large_k(self):
        self.assertEqual(caesarCipher("Always-Look-on-the-Bright-Side-of-Life", 87), "Jufjhb-Uxtt-xw-cqn-Karyqc-Bray-xo-Uron")

    def test_non_alphabet(self):
        self.assertEqual(caesarCipher("123 !@#", 10), "123 !@#")

    def test_zero_shift(self):
        self.assertEqual(caesarCipher("Hello-World", 0), "Hello-World")

    def test_wrap_around(self):
        self.assertEqual(caesarCipher("xyzXYZ", 3), "abcABC")