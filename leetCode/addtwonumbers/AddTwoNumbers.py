# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(0)
        curr = new_head
        carry = 0
        while l1 or l2 or carry != 0:
            la_val = l1.val if l1 else 0
            l2_ = l2.val if l2 else 0
            summing_vals = la_val + l2_ + carry
            carry = summing_vals // 10
            new_node = ListNode(summing_vals % 10)
            curr.next = new_node
            curr = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return new_head.next
