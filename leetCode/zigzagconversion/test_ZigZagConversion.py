from unittest import TestCase

from leetCode.zigzagconversion.ZigZagConversion import ZigZagConversion


class TestZigZagConversion(TestCase):
    def setUp(self):
        print(f"Running test: {self._testMethodName}")

    def test_zig_zag_the_string(self):
        zigzag = ZigZagConversion()
        self.assertEqual("PAHNAPLSIIGYIR", zigzag.zig_zag_the_string("PAYPALISHIRING", 3))
