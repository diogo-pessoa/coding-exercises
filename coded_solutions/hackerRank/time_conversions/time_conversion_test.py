from unittest import TestCase

from coded_solutions.hackerRank.timed_test.timed_test import findMedian


class TestMaxNonOverlappingSegments(TestCase):

  def test_findMedian(self):
    self.assertEqual(findMedian("07:05:45PM"), "19:05:45")
    self.assertEqual(findMedian("12:00:00AM"), "00:00:00")
    self.assertEqual(findMedian("12:00:00PM"), "12:00:00")
    self.assertEqual(findMedian("07:05:45AM"), "07:05:45")
    self.assertEqual(findMedian("11:59:59PM"), "23:59:59")
    self.assertEqual(findMedian("11:59:59AM"), "11:59:59")
    self.assertEqual(findMedian("01:00:00AM"), "01:00:00")
    self.assertEqual(findMedian("01:00:00PM"), "13:00:00")
    self.assertEqual(findMedian("12:00:00AM"), "00:00:00")
    self.assertEqual(findMedian("12:00:00PM"), "12:00:00")
    self.assertEqual(findMedian("12:00:00AM"), "00:00:00")
    self.assertEqual(findMedian("12:00:00PM"), "12:00:00")
    self.assertEqual(findMedian("12:00:00AM"), "00:00:00")
    self.assertEqual(findMedian("12:00:00PM"), "12:00:00")
    self.assertEqual(findMedian("12:00:00AM"), "00:00:00")
    self.assertEqual(findMedian("12:00:00PM"), "12:00:00")
    self.assertEqual(findMedian("12:00:00AM"), "00:00:00")
    self.assertEqual(findMedian("12:00:00PM"), "12:00:00")
    self.assertEqual(findMedian("12:00:00AM"), "00:00:00")
    self.assertEqual(findMedian("12:00:00PM"), "12:00:00")
    self.assertEqual(findMedian("12:00:00AM"), "00:00:00")
    self.assertEqual(findMedian("12:00:00PM"), "12:00:00")
    self.assertEqual(findMedian("12:00:00AM"), "00:00:00")
    self.assertEqual(findMedian("12:00:00PM"), "12:00:00")
