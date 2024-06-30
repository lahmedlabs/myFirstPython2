import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3, Calculator.add(2,1))
        self.assertEqual(Calculator.add(10, 5), 15)
        self.assertEqual(Calculator.add(-1, 1), 0)
        self.assertEqual(Calculator.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(10, 5), 5)
        self.assertEqual(Calculator.subtract(-1, 1), -2)
        self.assertEqual(Calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(10, 5), 50)
        self.assertEqual(Calculator.multiply(-1, 1), -1)
        self.assertEqual(Calculator.multiply(-1, -1), 1)
        self.assertEqual(Calculator.multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 5), 2)
        self.assertEqual(Calculator.divide(-1, 1), -1)
        self.assertEqual(Calculator.divide(-1, -1), 1)
        self.assertEqual(Calculator.divide(5, 2), 2.5)
        self.assertEqual(Calculator.divide(10, 0), "Error: Division by zero")


if __name__ == '__main__':
    unittest.main()
