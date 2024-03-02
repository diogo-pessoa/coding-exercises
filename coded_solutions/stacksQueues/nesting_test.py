from unittest import TestCase

from coded_solutions.stacksQueues.nesting import solution


class TestNesting(TestCase):
    def test_solution(self):
        S = "(()(())())"
        self.assertEqual(1, solution(S))

    def test_empty_string_returns_one(self):
        S = ""
        self.assertEqual(1, solution(S))

    def test_single_pair_of_parentheses_returns_one(self):
        S = "()"
        self.assertEqual(1, solution(S))

    def test_unbalanced_parentheses_returns_zero(self):
        S = "(()"
        self.assertEqual(0, solution(S))

    def test_multiple_balanced_pairs_returns_one(self):
        S = "()()()"
        self.assertEqual(1, solution(S))

    def test_nested_balanced_pairs_returns_one(self):
        S = "(())"
        self.assertEqual(1, solution(S))

    def test_vw_nested_strings(self):
        S = "(())()()"
        self.assertEqual(1, solution(S))