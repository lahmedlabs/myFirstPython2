from unittest import TestCase
import PrimeChecker
class Test(TestCase):
    # def test_is_prime(self):
    #     #self.fail()

    def test_prime_numbers_with2(self):
        self.assertTrue(PrimeChecker.is_prime(2))

    def test_prime_numbers_with3(self):
        self.assertTrue(PrimeChecker.is_prime(3))

    def test_prime_numbers_with5(self):
        self.assertTrue(PrimeChecker.is_prime(5))
    def test_prime_numbers_with29(self):
        self.assertTrue(PrimeChecker.is_prime(29))

    def test_non_prime_numbers_with1(self):
        self.assertFalse(PrimeChecker.is_prime(1))
    def test_prime_numbers_withMultpleOf2(self):
        self.assertFalse(PrimeChecker.is_prime(4))
        self.assertFalse(PrimeChecker.is_prime(30))
        self.assertFalse(PrimeChecker.is_prime(100))

    def test_edge_cases(self):
        self.assertFalse(PrimeChecker.is_prime(-1))
        self.assertFalse(PrimeChecker.is_prime(0))
        self.assertTrue(PrimeChecker.is_prime(97))  # 97 is a prime number
