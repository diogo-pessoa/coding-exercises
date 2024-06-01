from unittest import TestCase

from hackerRank.QueueAndStacks.queue_two_stacks import Queue as queue


class TestQueueTwoStacks(TestCase):
    def test_queue_two_stacks(self):
        operations = [[10], [1, 42], [2], [1, 14], [3], [1, 28], [3], [1, 60], [1, 78], [2], [2]]

        for query in operations:
            if query[0] == 1:
                queue.enqueue(query[1])
            elif query[0] == 2:
                queue.dequeue()
            elif query[0] == 3:
                print(queue.next_in_queue())
