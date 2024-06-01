import unittest

from hackerRank.find_uniq.find_uniq import lonelyinteger

class TestLonelyInteger(unittest.TestCase):
    def test_lonely_int(self):
        self.assertEqual(lonelyinteger([1, 2, 3, 4, 3, 2, 1]), 4)
        self.assertEqual(lonelyinteger([1, 2, 3, 4, 3, 2, 1, 4, 5, 5]), 0)
        self.assertEqual(lonelyinteger([1, 2, 3, 4, 3, 2, 1, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]), 10)
        self.assertEqual(lonelyinteger([1,2,3,4,5,5,4,2,1]), 3)

if __name__ == '__main__':
    unittest.main()
