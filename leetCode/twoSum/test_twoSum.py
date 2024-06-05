from unittest import TestCase

from twoSum import TwoSum


class TestSolution(TestCase):
    def test_two_sum(self):
        # Test case 1
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        print(TwoSum().two_sum(nums, target))
        self.assertEqual(TwoSum().two_sum(nums, target), expected)

        # Test case 2
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        self.assertEqual(TwoSum().two_sum(nums, target), expected)

        # Test case 3
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        self.assertEqual(TwoSum().two_sum(nums, target), expected)

    def test_two_sum_skipped(self):
        nums = [3, 2, 3]
        target = 6
        expected = [0, 2]
        print(TwoSum().two_sum(nums, target))
        self.assertEqual(TwoSum().two_sum(nums, target), expected)
