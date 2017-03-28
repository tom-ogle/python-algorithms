import unittest
from unittest import TestCase
from sorting.insertion_sort import insertion_sort


class TestInsertionSort(TestCase):
    def test_insertion_sort(self):
        input = "INSERTIONSORT"
        expected_result = ['E', 'I', 'I', 'N', 'N', 'O', 'O', 'R', 'R', 'S', 'S', 'T', 'T']
        actual_result = insertion_sort(input)
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()
