import unittest
from Calculator import Calculator
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator=Calculator()
    def testAdd(self):
        self.assertEqual(self.calculator.add(5, 4) ,9,'Incorrect') 
    def testSubtract(self):
        self.assertEqual(self.calculator.subtract(8, 2) ,6,'Incorrect')