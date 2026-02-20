from coe_number.number_utils import is_prime_list
import unittest
class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [7, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_2_3_5_is_prime(self):
        prime_list = [2, 3, 5]
        self.assertTrue(is_prime_list(prime_list))

    def test_give_2_4_6_is_not_prime(self):
        prime_list = [2, 4, 6]
        self.assertFalse(is_prime_list(prime_list))

    def test_give_1_is_not_prime(self):
        prime_list = [1]
        self.assertFalse(is_prime_list(prime_list))

    def test_give_large_primes_is_prime(self):
        prime_list = [13, 17, 19, 23]
        self.assertTrue(is_prime_list(prime_list))

    def test_give_empty_list_is_not_prime(self):
        prime_list = []
        self.assertFalse(is_prime_list(prime_list))