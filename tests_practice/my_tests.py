import unittest
from unittest.mock import patch

from functions import *


class Test(unittest.TestCase):

    def test_func1(self):
        expected = [1, 2, 3, 5, 8, 13]
        self.assertEqual(func1(), expected)

    def test_func2(self):
        excpected = 5
        self.assertEqual(func2(), excpected)

    def test_func3(self):
        self.assertTrue(func3(27))
        self.assertFalse(func3(333))

    def test_func4(self):
        expected_result = 5
        self.assertEqual(func4(59), expected_result)

    def test_func5(self):
        a = func5([1, 2, 3, 4, 0, 5, 0, 6])
        expected = [1, 2, 3, 4, 5, 6, 0, 0]
        self.assertEqual(a, expected)

    def test_func6(self):
        a = func6([5, 7, 9, 11])
        b = func6([1, 23, 6, 4])
        self.assertTrue(a)
        self.assertFalse(b)

    def test_func7(self):
        expected_result = 9
        actual_result = func7([5, 3, 4, 3, 4, 5, 9])
        self.assertEqual(actual_result, expected_result)

    def test_func8(self):
        expected_result = 6
        actual_result = func8([1, 2, 3, 4, 5, 7, 8])
        self.assertEqual(actual_result, expected_result)

    def test_func9(self):
        expected_result = 2
        actual_result = func9([211, 582, (1, 2), 3])
        self.assertEqual(expected_result, actual_result)

    def test_func10(self):
        expected_result = 'sredoC dna dlroW olleH'
        actual_result = func10('Hello World and Coders')
        self.assertEqual(expected_result, actual_result)

    def test_func11(self):
        expected_result = '1:3'
        actual_result = func11(63)
        self.assertEqual(actual_result, expected_result)

    def test_func12_1(self):
        expected_result = 'summer'
        actual_result = func12('I love summer')
        self.assertEqual(actual_result, expected_result)

    def test_func12_2(self):
        expected_result = 'time'
        actual_result = func12('fun&!! time')
        self.assertEqual(actual_result, expected_result)

    @patch("functions.func13", return_value='Michele is name My')
    def test_func13(self, func13):
        self.assertEqual(func13(), 'Michele is name My')

    @patch("functions.func14", return_value='1, 1, 2, 3')
    def test_func14(self, func14):
        self.assertEqual(func14(), '1, 1, 2, 3')

    def test_func15(self):
        a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        actual_result = func15(a)
        expected_result = [4, 16, 36, 64, 100]
        self.assertEqual(actual_result, expected_result)

    def test_func16(self):
        actual_result = func16(4)
        expected_result = 10
        self.assertEqual(actual_result, expected_result)

    def test_func17(self):
        actual_result = func17(4)
        expected_result = 24
        self.assertEqual(expected_result, actual_result)

    def test_func18(self):
        actual_result = func18('abcdz')
        expected_result = 'bcdEA'
        self.assertEqual(actual_result, expected_result)

    def test_func19(self):
        actual_result = func19('edcba')
        expected_result = 'abcde'
        self.assertEqual(expected_result, actual_result)

    def test_func20(self):
        self.assertTrue(func20(2, 5))
        self.assertFalse(func20(5, 2))

    def test_func20_equal(self):
        self.assertEqual(func20(2, 2), '-1')


if __name__ == '__main__':
    unittest.main()
