from helpers.TimeItDecorator import timeit_decorator


class QuickSort:
    """
    Divide and conquer algorithm. It picks an element as pivot and partitions the
    given array around the picked pivot.
    Pivot - function
    """

    def _pivot_by_first_element(self, partition, pivot_index, end_index):
        """
        pivot by first element in the partition
        :param partition:
        :param pivot_index:
        :param end_index:
        :return:
        """
        swap_index = pivot_index

        for i in range(pivot_index + 1, end_index + 1):
            if partition[i] < partition[pivot_index]:
                swap_index += 1
                self._swap(partition, swap_index, i)
        self._swap(partition, pivot_index, swap_index)
        return swap_index

    def _swap(self, partition, i, j):
        temporary = partition[i]
        partition[i] = partition[j]
        partition[j] = temporary

    @timeit_decorator
    def quick_sort_first_el(self, list_to_sort, left_index, right_index):
        """
        Quicksort Algorithm using self._pivot_by_first_element
        :param list_to_sort:
        :param left_index:
        :param right_index:
        :return:
        """
        if len(list_to_sort) <= 1:
            return list_to_sort
        if left_index < right_index:
            pivot_index = self._pivot_by_first_element(list_to_sort, left_index,
                                                       right_index)
            # sort left side partition - from pivot
            self.quick_sort_first_el(list_to_sort, left_index, pivot_index - 1)
            # sort right side partition - from pivot
            self.quick_sort_first_el(list_to_sort, pivot_index + 1, right_index)
        return list_to_sort

    def _pivot_by_median_of_three(self, list_to_sort, left_index, right_index):
        """
        pivot by median of three elements in the partition
        :param list_to_sort:
        :param left_index:
        :param right_index:
        :return:
        """
        first_element = list_to_sort[left_index]
        middle_element = list_to_sort[(left_index + right_index) // 2]
        last_element = list_to_sort[right_index]
        pivot = sorted([first_element, middle_element, last_element])[1]
        lesser_partition = [value for value in list_to_sort if value < pivot]
        greater_partition = [value for value in list_to_sort if value > pivot]
        equal_partition = [value for value in list_to_sort if value == pivot]
        return lesser_partition, equal_partition, greater_partition

    @timeit_decorator
    def quick_sort_medians_of_threes(self, list_to_sort, left_index, right_index):
        """
        Quicksort Algorithm using self._pivot_by_median_of_three
        :return:
        """
        if len(list_to_sort) <= 1:
            return list_to_sort

        lesser_partition, equal_partition, greater_partition = (
            self._pivot_by_median_of_three(list_to_sort, left_index, right_index))

        # For readability, I'm breaking the recursion into two lines, instead of all
        # in the return
        sorted_lesser_partition = self.quick_sort_medians_of_threes(lesser_partition,
                                                                    left_index,
                                                                    len(lesser_partition) - 1)
        sorted_greater_partition = self.quick_sort_medians_of_threes(greater_partition,
                                                                     left_index,
                                                                     len(greater_partition) - 1)
        return sorted_lesser_partition + equal_partition + sorted_greater_partition()
