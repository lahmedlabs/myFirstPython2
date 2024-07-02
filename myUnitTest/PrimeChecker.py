# 소수 prime number 인지를 판정하는 함수
# 소수(prime number)는 1과 자기 자신만을 약수로 가지는 1보다 큰 자연수
def is_prime(n):
    if n <= 1:          # 1 이하이면 소수 아님
        return False
    if n == 2:          # 2이면 소수
        return True
    if n % 2 == 0:      # 2가 아닌 짝수이면 소수가 아님
        return False
    # n이 홀수이면 3부터 n의 제곱근까지의 홀수로 나누어 떨어지면 소수 아님
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# # 테스트 케이스
# print(is_prime(1))  # False
# print(is_prime(2))  # True
# print(is_prime(3))  # True
# print(is_prime(4))  # False
# print(is_prime(5))  # True
# print(is_prime(29)) # True
# print(is_prime(30)) # False
#
# # unittest 이용
# import unittest
#
# class TestPrimeFunction(unittest.TestCase):
#
#     def test_prime_numbers(self):
#         self.assertTrue(is_prime(2))
#         self.assertTrue(is_prime(3))
#         self.assertTrue(is_prime(5))
#         self.assertTrue(is_prime(29))
#
#     def test_non_prime_numbers(self):
#         self.assertFalse(is_prime(1))
#         self.assertFalse(is_prime(4))
#         self.assertFalse(is_prime(30))
#         self.assertFalse(is_prime(100))
#
#     def test_edge_cases(self):
#         self.assertFalse(is_prime(-1))
#         self.assertFalse(is_prime(0))
#         self.assertTrue(is_prime(97))  # 97 is a prime number
#
# if __name__ == '__main__':
#     unittest.main()
