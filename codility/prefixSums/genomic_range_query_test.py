from unittest import TestCase

from codility.genomic_range_query import genomic_range_query


class TestGenomicRangeQuery(TestCase):
    def test_genomic_range_query(self):
        P = [2, 5, 0]
        Q = [4, 5, 6]
        S = 'CAGCCTA'
        self.assertEqual([2, 4, 1], genomic_range_query(S, P, Q))
