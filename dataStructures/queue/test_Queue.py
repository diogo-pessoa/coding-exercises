from unittest import TestCase

from dataStructures.queue.Queue import Queue


class TestQueue(TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(2)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 2)

    def test_peek(self):
        queue = Queue()
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.peek(), 2)

    def test_size(self):
        queue = Queue()
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.size(), 2)

    def test_is_empty(self):
        queue = Queue()
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertFalse(queue.is_empty())
        queue.dequeue()
        queue.dequeue()
        self.assertTrue(queue.is_empty())
