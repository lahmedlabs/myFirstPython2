#class Calculator:
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


#import unittest

# test code
# class TestCalculator(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(Calculator.add(10, 5), 15)
#         self.assertEqual(Calculator.add(-1, 1), 0)
#         self.assertEqual(Calculator.add(-1, -1), -2)
#
#     def test_subtract(self):
#         self.assertEqual(Calculator.subtract(10, 5), 5)
#         self.assertEqual(Calculator.subtract(-1, 1), -2)
#         self.assertEqual(Calculator.subtract(-1, -1), 0)