import unittest
from passing_cars import counting_cars_1

class TestCountingCars(unittest.TestCase):
    def test_cars_in_empty_list(self):
        result = counting_cars_1([])
        self.assertEqual(result, 0)

    def test_cars_in_single_element_list(self):
        result = counting_cars_1([1])
        self.assertEqual(result, 1)

    @unittest.skip("Skip this test- not on challenge")
    def test_cars_in_two_element_list(self):
        result = counting_cars_1([1, 0])
        self.assertEqual(result, 1)

    def test_cars_in_large_list(self):
        result = counting_cars_1([1]*1000000000)
        self.assertEqual(result, -1)

    @unittest.skip("Skip this test- not on challenge")
    def test_cars_in_list_with_negative_numbers(self):
        result = counting_cars_1([-1, 0, 1])
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()