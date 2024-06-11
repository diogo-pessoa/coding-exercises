from unittest import TestCase

from algorithms.mergesort.MergeSort import MergeSort


class TestMergeSort(TestCase):
    def test_dumb_merge(self):
        merge_sort = MergeSort()
        list_b = [1, 3, 5]
        list_a = [2, 4, 6]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(expected, merge_sort.dumb_merge(list_a, list_b))

    def test_merge_sort(self):
        merge_sort = MergeSort()
        list_to_sort = [1, 3, 5, 2, 4, 6]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(expected, merge_sort.merge_sort(list_to_sort))
