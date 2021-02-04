import unittest
import calculator



class TestCase(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator.addition(2,1), 3)
        self.assertEqual(calculator.addition(-5,3), -2)
        self.assertEqual(calculator.addition(-5,0), -5)
        self.assertEqual(calculator.addition(-5.5,10), 4.5)
    def test_subtraction(self):
        self.assertEqual(calculator.subtraction(2,1), 1)
        self.assertEqual(calculator.subtraction(2,1.5), .5)
        self.assertEqual(calculator.subtraction(5,5), 0)
        self.assertEqual(calculator.subtraction(5,8), -3)
    
    def test_multiplication(self):
        self.assertEqual(calculator.multiplication(2, 1), 2)
        self.assertEqual(calculator.multiplication(2, 0), 0)
        self.assertEqual(calculator.multiplication(2, -6), -12)
        self.assertAlmostEqual(calculator.multiplication(2, 3.33), 6.66)
    

    def test_diviision(self):
        self.assertEqual(calculator.division(2,1), 2)
        self.assertEqual(calculator.division(8,4), 2)
        self.assertEqual(calculator.division(-10,-2), 5)
        self.assertEqual(calculator.division(9,2.5), 3.6)
    def test_divbyzero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.division(2, 0)


if __name__ == '__main__':
    unittest.main()