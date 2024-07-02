from unittest import TestCase
import Palindrome

class Test(TestCase):
    def test_palindrome_true(self):
        self.assertTrue(Palindrome.is_palindrome("A man, a plan, a canal, Panama"))

    # 테스트 케이스
    def test_palindrome_false(self):
        self.assertFalse(Palindrome.is_palindrome("hello"))


# print(is_palindrome(""))  # True
# print(is_palindrome("racecar"))  # True
# print(is_palindrome("hello"))  # False
# print(is_palindrome("12321"))  # True
# print(is_palindrome("No lemon, no melon"))  # True


