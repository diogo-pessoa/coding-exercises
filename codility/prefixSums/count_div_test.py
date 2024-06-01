import unittest

from count_div import solution_1


class TestCountingCars(unittest.TestCase):
    def test_count_div(self):
        a = 6
        b = 11
        k = 2

        self.assertEqual(solution_1(a, b, k), 3)

    def test_division_in_empty_range(self):
        result = solution_1(0, 0, 1)
        self.assertEqual(result, 1)

    def test_division_in_single_element_range(self):
        result = solution_1(1, 1, 1)
        self.assertEqual(result, 1)

    def test_division_in_two_element_range(self):
        result = solution_1(1, 2, 1)
        self.assertEqual(result, 2)

    def test_division_in_large_range(self):
        result = solution_1(1, 1000000000, 1)
        self.assertEqual(result, 1000000000)

    def test_division_in_range_with_negative_numbers(self):
        result = solution_1(-1, 1, 1)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
