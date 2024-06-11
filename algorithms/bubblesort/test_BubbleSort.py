import random
from unittest import TestCase

from algorithms.bubblesort.BubbleSort import BubbleSort


class TestBubbleSort(TestCase):

    def setUp(self):
        self.bubble_sort = BubbleSort()
        self.list_to_sort = [random.randint(1, 10000) for _ in
                             range(random.randint(10, 4000))]
        self.list_to_sort_2 = self.list_to_sort.copy()
        print(f"Running test: {self._testMethodName}")

    def test_sort_two_loops(self):
        list_to_sort = [random.randint(1, 10000) for _ in
                        range(random.randint(10, 4000))]
        print(f"Unsorted list: {len(list_to_sort)}")
        self.bubble_sort.sort_double_for(list_to_sort)

        self.assertTrue(self.bubble_sort.is_sorted(list_to_sort))

    def test_sort_one_loop(self):
        list_to_sort = [random.randint(1, 10000) for _ in
                        range(random.randint(10, 4000))]
        print(f"Unsorted list len: {len(list_to_sort)}")
        self.bubble_sort.sort_while(list_to_sort)
        self.assertTrue(self.bubble_sort.is_sorted(list_to_sort))

    def test_running_both_sorts(self):
        print(f"list len: {len(self.list_to_sort)}")
        self.bubble_sort.sort_while(self.list_to_sort)
        self.bubble_sort.sort_double_for(self.list_to_sort_2)
        self.assertTrue(self.bubble_sort.is_sorted(self.list_to_sort))
        self.assertTrue(self.bubble_sort.is_sorted(self.list_to_sort_2))
