class MergeSort:

    @staticmethod
    def dumb_merge(list_a, list_b):
        combined_list = []
        i, j = 0, 0
        while i < len(list_a) and j < len(list_b):
            if list_a[i] < list_b[j]:
                combined_list.append(list_a[i])
                i += 1
            else:
                combined_list.append(list_b[j])
                j += 1
        while i < len(list_a):
            combined_list.append(list_a[i])
            i += 1
        while j < len(list_b):
            combined_list.append(list_b[j])
            j += 1
        return combined_list

    def merge_sort(self, list_to_sort):
        """
        Using Recursion merge the list
        time complexity: O(n log n)
        space complexity: O(n)
        :param list_to_sort:
        :return:
        """
        if len(list_to_sort) <= 1:
            return list_to_sort
        mid = len(list_to_sort) // 2
        left = self.merge_sort(list_to_sort[:mid])
        right = self.merge_sort(list_to_sort[mid:])
        return self.dumb_merge(left, right)