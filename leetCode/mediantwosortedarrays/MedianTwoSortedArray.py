from algorithms.mergesort.MergeSort import MergeSort
from helpers.TimeItDecorator import timeit_decorator


class MedianTwoSortedArrays:

    @staticmethod
    @timeit_decorator
    def find_median_binary_search(nums1, nums2) -> float:
        # TODO - In progress
        """
        If m + n is odd, we are looking for the (m + n) / 2-th element.
        If m + n is even, we are looking for the average of the (m + n) / 2-th and
        the (m + n) / 2 + 1-th elements.

        :param nums1:
        :param nums2:
        :return:
        """
        pass

    @staticmethod
    def find_median_merge_list(nums1, nums2) -> float:
        """
        Merge two sorted arrays and return the median
        calling method from MergeSort class.
        Note: I don't need to sort the arrays(they're already sorted), just merge them.
        Then, calculate the median
        :param nums1:
        :param nums2:
        :return:
        """
        merge = MergeSort()
        combined_list = merge.dumb_merge(nums1, nums2)
        n = len(combined_list)
        if n % 2 == 0:
            return (combined_list[n // 2 - 1] + combined_list[n // 2]) / 2
        else:
            return combined_list[n // 2]
