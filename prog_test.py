import unittest
from prog import divide

class TestDivide(unittest.TestCase):

    def test_normal(self):   
        self.assertEqual(divide(10,5),2)

    def test_divide_by_zero(self):   
        self.assertIsNone(divide(10,0))

    def test_divide_float(self):   
        self.assertAlmostEqual(divide(7,2),3.5)

    def value_error(self):  
        self.assertRaises(ValueError):
        

if __name__ == "__main__":
    unittest.main()


    