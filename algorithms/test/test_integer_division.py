import unittest
from unittest import TestCase

from misc.integer_division import integer_division_recursive, integer_division_iterative


class TestIntegerDivisionRecursive(TestCase):
    def test_y_less_than_x(self):
        x = 5
        y = 2
        expected_result = 2
        actual_result = integer_division_recursive(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_y_greater_than_x(self):
        x = 3
        y = 4
        expected_result = 0
        actual_result = integer_division_recursive(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_y_equal_to_x(self):
        x = 4
        y = 4
        expected_result = 1
        actual_result = integer_division_recursive(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_negative_y_positive_x_no_remainder(self):
        x = 4
        y = -2
        expected_result = -2
        actual_result = integer_division_recursive(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_negative_y_positive_x_remainder(self):
        x = 4
        y = -3
        expected_result = -1
        actual_result = integer_division_recursive(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_positive_y_negative_x_no_remainder(self):
        x = -6
        y = 2
        expected_result = -3
        actual_result = integer_division_recursive(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_positive_y_negative_x_remainder(self):
        x = -7
        y = 2
        expected_result = -3
        actual_result = integer_division_recursive(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_negative_y_negative_x_no_remainder(self):
        x = -6
        y = -2
        expected_result = 3
        actual_result = integer_division_recursive(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_negative_y_negative_x_remainder(self):
        x = -7
        y = -2
        expected_result = 3
        actual_result = integer_division_recursive(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_divide_by_zero_y(self):
        x = 8
        y = 0
        with self.assertRaises(ZeroDivisionError):
            integer_division_recursive(x, y)

    def test_divide_zero_x(self):
        x = 0
        y = 2
        expected_result = 0
        actual_result = integer_division_recursive(x, y)
        self.assertEqual(expected_result, actual_result)


class TestIntegerDivisionIterative(TestCase):
    def test_y_less_than_x(self):
        x = 5
        y = 2
        expected_result = 2
        actual_result = integer_division_iterative(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_y_greater_than_x(self):
        x = 3
        y = 4
        expected_result = 0
        actual_result = integer_division_iterative(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_y_equal_to_x(self):
        x = 4
        y = 4
        expected_result = 1
        actual_result = integer_division_iterative(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_negative_y_positive_x_no_remainder(self):
        x = 4
        y = -2
        expected_result = -2
        actual_result = integer_division_iterative(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_negative_y_positive_x_remainder(self):
        x = 4
        y = -3
        expected_result = -1
        actual_result = integer_division_iterative(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_positive_y_negative_x_no_remainder(self):
        x = -6
        y = 2
        expected_result = -3
        actual_result = integer_division_iterative(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_positive_y_negative_x_remainder(self):
        x = -7
        y = 2
        expected_result = -3
        actual_result = integer_division_iterative(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_negative_y_negative_x_no_remainder(self):
        x = -6
        y = -2
        expected_result = 3
        actual_result = integer_division_iterative(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_negative_y_negative_x_remainder(self):
        x = -7
        y = -2
        expected_result = 3
        actual_result = integer_division_iterative(x, y)
        self.assertEqual(expected_result, actual_result)

    def test_divide_by_zero_y(self):
        x = 8
        y = 0
        with self.assertRaises(ZeroDivisionError):
            integer_division_iterative(x, y)

    def test_divide_zero_x(self):
        x = 0
        y = 2
        expected_result = 0
        actual_result = integer_division_iterative(x, y)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()