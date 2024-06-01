import unittest


class TestZigZag(unittest.TestCase):
    def test_zig_zag(self):
        self.assertEqual(findZigZagSequence([1, 2, 3, 4, 5, 6, 7], 1), None)  # add assertion here


if __name__ == '__main__':
    unittest.main()
