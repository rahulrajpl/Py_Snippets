import unittest
import Unit_Testing_in_Python


class TestUnitTesting(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Unit_Testing_in_Python.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(Unit_Testing_in_Python.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(Unit_Testing_in_Python.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(Unit_Testing_in_Python.divide(10, 5), 2)
        self.assertRaises(ValueError, Unit_Testing_in_Python.divide, 10, 0)
        # Testing exceptions can be done using context manager as below
        with self.assertRaises(ValueError):
            Unit_Testing_in_Python.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
    date = set()