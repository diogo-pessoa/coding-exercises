from helpers.TimeItDecorator import timeit_decorator


class BubbleSort:

    @staticmethod
    @timeit_decorator
    def sort_double_for(list_to_sort):
        n = len(list_to_sort)
        for i in range(n):
            for j in range(0, n - i - 1):
                if list_to_sort[j] > list_to_sort[j + 1]:
                    list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], \
                        list_to_sort[j]
        return list_to_sort

    @staticmethod
    @timeit_decorator
    def sort_while(list_to_sort):
        n = len(list_to_sort)
        while True:
            swapped = False
            for i in range(n - 1):
                if list_to_sort[i] > list_to_sort[i + 1]:
                    list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], \
                        list_to_sort[i]
                    swapped = True
            if not swapped:
                break
            n -= 1  # Reduce the range for the next pass
        return list_to_sort

    # Function to check if a list is sorted
    @staticmethod
    def is_sorted(bubbled_list):
        """
        Big O: O(n)
        :param bubbled_list:
        :return:
        """
        return all(bubbled_list[i] <= bubbled_list[i + 1] for i in
                   range(len(bubbled_list) - 1))
