from unittest import TestCase

from algorithms.quicksort.QuickSort import QuickSort


class TestQuickSort(TestCase):
    # TODO - add test cases for _pivot_by_first_element, _pivot_by_median_of_three
    def setUp(self):
        print(f"Running test: {self._testMethodName}")
        self.quick_sort = QuickSort()

    def test__quick_sort_by_first_element(self):
        list_to_sort = [10, 7, 8, 9, 1, 5]
        self.quick_sort.quick_sort_first_el(list_to_sort, 0, (len(list_to_sort) - 1))
        self.assertEqual(list_to_sort, [1, 5, 7, 8, 9, 10])

    def test__quick_sort_by_median_of_three(self):
        list_to_sort = [10, 7, 8, 9, 1, 5]
        self.quick_sort.quick_sort_medians_of_threes(list_to_sort, 0,
                                                     (len(list_to_sort) - 1))
        self.assertEqual(list_to_sort, [1, 5, 7, 8, 9, 10])

    def test__swap(self):
        list_to_swap = [1, 2, 3, 4]
        self.quick_sort._swap(list_to_swap, 0, 3)
        self.assertEqual(list_to_swap, [4, 2, 3, 1])
