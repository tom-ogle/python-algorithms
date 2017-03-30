import unittest
from unittest import TestCase

from sorting.selection_sort import selection_sort


class TestSelectionSort(TestCase):
    def test_insertion_sort(self):
        to_sort = list("SELECTIONSORT")
        expected_result = list("CEEILNOORSSTT")
        actual_result = selection_sort(to_sort)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
