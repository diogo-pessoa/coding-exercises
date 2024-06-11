class QuickSort:
    """
    Divide and conquer algorithm. It picks an element as pivot and partitions the
    given array around the picked pivot.
    Pivot - function
    """

    def _pivot(self, partition, pivot_index, end_index):
        swap_index = pivot_index

        for i in range(pivot_index + 1, end_index + 1):
            if partition[i] <= partition[pivot_index]:
                swap_index += 1
                self._swap(partition, swap_index, i)
        self._swap(partition, pivot_index, swap_index)
        return swap_index

    def _swap(self, partition, i, j):
        temporary = partition[i]
        partition[i] = partition[j]
        partition[j] = temporary
