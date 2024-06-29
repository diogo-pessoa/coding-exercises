from unittest import TestCase

from MapTransform import MapTransform


class TestMapFilterReduce(TestCase):
    """
        Studying built-in map() and a use-case I could face in the day-to-day.
        """
    def setUp(self):
        print(f"Running Test: {self._testMethodName}")
        self.map_filter_reduce = MapTransform()

    def test_mapping_built_in(self):
        numbers = [1, 2, 3, 4]
        squared = map(lambda x: x ** 2, numbers)
        print(type(squared))
        print(list(squared))
        print(squared.__doc__)

    def test_mapping_filtering_filter_for_even_numbers(self):
        numbers = [1, 2, 3, 4]
        filtered_nums = filter(lambda x: x % 2 == 0, numbers)
        squared = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
        print(type(filtered_nums))
        print(list(filtered_nums))
        print("resulting map: ", list(squared))
        print(filtered_nums.__doc__)

    def test_transform_keys(self):
        string_to_transform = {'KeyFor#testing': 'value', 'KeyFor#second_test': 'value2'}
        result = self.map_filter_reduce.transform_keys(string_to_transform)
        self.assertEqual(result, [('testing', 'value'), ('second_test', 'value2')])
