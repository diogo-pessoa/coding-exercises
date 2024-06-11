from helpers.TimeItDecorator import timeit_decorator


class LongString:

    def __init__(self, long_string: str):
        self.char_map = {}
        self._load_string(long_string)

    @timeit_decorator
    def _load_string(self, long_string: str):
        """
        Load string into char_map, by storing the index of each character within the
        char key
        :param long_string:
        :return:
        """

        for i, c in enumerate(long_string):
            if c in self.char_map:
                self.char_map[c].append(i)
            else:
                self.char_map[c] = [long_string.index(c)]

    @timeit_decorator
    def custom_compares(self, string_to_check) -> bool:
        """
        Compares the LongSting char_map - and index len for each character

        :param string_to_check: LongString Object
        :return:
        """
        # First case if the hash doesn't have the same keys - return False
        if self.char_map.keys() != string_to_check.char_map.keys():
            return False
        return self.compare_each_char_map_length(string_to_check)

    def compare_each_char_map_length(self, string_to_check):
        """
        Compare the char_map of the LongString object
        :param string_to_check:
        :return:
        """

        for k, v in self.char_map.items():
            if k not in string_to_check.char_map:
                return False
            if len(v) != len(string_to_check.char_map[k]):
                return False
        return True

    @staticmethod
    @timeit_decorator
    def using_string_comparison(original_string, string_to_check) -> bool:
        """
        Naive compare of strings, O(n)
        :param original_string:
        :param string_to_check:
        :return:
        """
        return original_string == string_to_check

    def edit(self):
        # TODO - Implement this method
        pass
