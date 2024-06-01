from unittest import TestCase

from codility.stacksQueues.brackets import solution

class TestBrackets(TestCase):
    def test_solution(self):
        S = "{[()()]}"
        self.assertEqual(1, solution(S))
    
    def test_solution_1(self):
        S = "([)()]"
        self.assertEqual(0, solution(S))

    def test_solution_handles_empty_string(self):
        S = ""
        self.assertEqual(1, solution(S))

    def test_solution_handles_single_bracket(self):
        S = "("
        self.assertEqual(0, solution(S))

    def test_solution_handles_unbalanced_brackets(self):
        S = "{[()]"
        self.assertEqual(0, solution(S))

    def test_solution_handles_balanced_brackets_without_nesting(self):
        S = "{}[]()"
        self.assertEqual(1, solution(S))

    def test_solution_handles_unbalanced_brackets_with_extra_closing(self):
        S = "{[()()]}}"
        self.assertEqual(0, solution(S))

    def test_solution_handles_unbalanced_brackets_with_extra_opening(self):
        S = "{{[()()]}"
        self.assertEqual(0, solution(S))