from unittest import TestCase

from leetCode.mediantwosortedarrays.MedianTwoSortedArray import MedianTwoSortedArrays


class TestMedianTwoSortedArrays(TestCase):

    def setUp(self):
        self.median_two_arrays = MedianTwoSortedArrays()

    def test_find_median(self):
        self.assertEqual(self.median_two_arrays.find_median_naive([1, 3], [2]), 2.0)
        self.assertEqual(self.median_two_arrays.find_median_naive([1, 2], [3, 4]), 2.5)
        # TODO - This test runs forever (refactoring required)
        self.assertEqual(self.median_two_arrays.find_median_naive([0, 0], [0, 0]), 0.0)

    def test_find_median_binary_search_tree(self):
        # TODO - In progress
        pass

    def test_find_median_merge(self):
        list_a = [1, 3, 5]
        list_b = [2, 4, 6]
        self.assertEqual(self.median_two_arrays.find_median_merge_list([1, 2], [3, 4]), 2.5)
        self.assertEqual(self.median_two_arrays.find_median_merge_list([0, 0], [0, 0]),
                         0)
        self.assertEqual(self.median_two_arrays.find_median_merge_list([1, 3], [2]), 2.0)

