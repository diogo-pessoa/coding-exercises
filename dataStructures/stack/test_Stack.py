from unittest import TestCase

from dataStructures.stack.Stack import Stack


class TestStack(TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(2)
        self.assertEqual(stack.stack, [2])

    def test_pop(self):
        stack = Stack()
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)

    def test_peek(self):
        stack = Stack()
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)

    def test_size(self):
        stack = Stack()
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.size(), 2)

    def test_is_empty(self):
        stack = Stack()
        stack.push(2)
        stack.push(3)
        self.assertFalse(stack.is_empty())
        stack.pop()
        stack.pop()
        self.assertTrue(stack.is_empty())
