import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_add(self):
        self.assertEqual(self.calculator.add(5,8), 12)
                            #Здесь должна быть ошибка
    def test_minus(self):
        self.assertEqual(self.calculator.minus(5,3), 2)
    def test_divide(self):
        self.assertEqual(self.calculator.divide(10,2), 5)
    def test_divideZero(self):
        self.assertEqual(self.calculator.divide(10,0), msg="Error")
        #Здесь должна быть ошибка
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3,4), 12)
if __name__ == "__main__":
    unittest.main()