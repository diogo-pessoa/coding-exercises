from typing import Optional
from unittest import TestCase

from leetCode.addtwonumbers.AddTwoNumbers import Solution, ListNode


class TestAddTwoNumbers(TestCase):
    def test_add_two_numbers(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        expected = ListNode(7, ListNode(0, ListNode(8)))
        solution = Solution()
        actual = solution.add_two_numbers(l1, l2)
        self.assertEqual(expected.val, actual.val)
        self.assertEqual(expected.next.val, actual.next.val)
        self.assertEqual(expected.next.next.val, actual.next.next.val)
        self.assertIsNone(actual.next.next.next)
