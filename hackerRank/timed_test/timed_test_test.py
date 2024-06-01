
from unittest import TestCase

from hackerRank.timed_test.timed_test import findMedian


class TestTimedTest(TestCase):

    def test_timedTest(self):
        self.assertEqual(findMedian([0, 1, 2, 4, 6, 5, 3]), 3)
