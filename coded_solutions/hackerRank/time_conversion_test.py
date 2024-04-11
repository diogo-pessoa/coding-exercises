from unittest import TestCase

from coded_solutions.hackerRank.time_conversion import timeConversion


class TestMaxNonOverlappingSegments(TestCase):

  def test_timeConversion(self):
    self.assertEqual(timeConversion("07:05:45PM"), "19:05:45")
    self.assertEqual(timeConversion("12:00:00AM"), "00:00:00")
    self.assertEqual(timeConversion("12:00:00PM"), "12:00:00")
    self.assertEqual(timeConversion("07:05:45AM"), "07:05:45")
    self.assertEqual(timeConversion("11:59:59PM"), "23:59:59")
    self.assertEqual(timeConversion("11:59:59AM"), "11:59:59")
    self.assertEqual(timeConversion("01:00:00AM"), "01:00:00")
    self.assertEqual(timeConversion("01:00:00PM"), "13:00:00")
    self.assertEqual(timeConversion("12:00:00AM"), "00:00:00")
    self.assertEqual(timeConversion("12:00:00PM"), "12:00:00")
    self.assertEqual(timeConversion("12:00:00AM"), "00:00:00")
    self.assertEqual(timeConversion("12:00:00PM"), "12:00:00")
    self.assertEqual(timeConversion("12:00:00AM"), "00:00:00")
    self.assertEqual(timeConversion("12:00:00PM"), "12:00:00")
    self.assertEqual(timeConversion("12:00:00AM"), "00:00:00")
    self.assertEqual(timeConversion("12:00:00PM"), "12:00:00")
    self.assertEqual(timeConversion("12:00:00AM"), "00:00:00")
    self.assertEqual(timeConversion("12:00:00PM"), "12:00:00")
    self.assertEqual(timeConversion("12:00:00AM"), "00:00:00")
    self.assertEqual(timeConversion("12:00:00PM"), "12:00:00")
    self.assertEqual(timeConversion("12:00:00AM"), "00:00:00")
    self.assertEqual(timeConversion("12:00:00PM"), "12:00:00")
    self.assertEqual(timeConversion("12:00:00AM"), "00:00:00")
    self.assertEqual(timeConversion("12:00:00PM"), "12:00:00")
