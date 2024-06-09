from unittest import TestCase

from dataStructures.graph.GraphAdMatrix import GraphAdMatrix


class TestGraphAdMatrix(TestCase):
    def test_add_cannon_event(self):
        spider_verse = GraphAdMatrix(5)
        spider_verse.add_cannon_event(0)
        spider_verse.add_cannon_event(1)
        spider_verse.add_cannon_event(2)
        spider_verse.show_multiverse()
        self.assertEqual(spider_verse.multiverse,
                         [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    def test_remove_cannon_event(self):
        spider_verse = GraphAdMatrix(5)
        spider_verse.add_cannon_event(0)
        spider_verse.add_cannon_event(1)
        spider_verse.add_cannon_event(2)
        spider_verse.remove_cannon_event(2, 2)
        spider_verse.show_multiverse()
        self.assertEqual(spider_verse.multiverse,
                         [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    def test_add_connection(self):
        spider_verse = GraphAdMatrix(5)
        spider_verse.add_cannon_event(0)
        spider_verse.add_cannon_event(1)
        spider_verse.add_cannon_event(2)
        spider_verse.add_connection(0, 1)
        spider_verse.show_multiverse()
        self.assertEqual(spider_verse.multiverse,
                         [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    def test_remove_connection(self):
        spider_verse = GraphAdMatrix(5)
        spider_verse.add_cannon_event(0)
        spider_verse.add_cannon_event(1)
        spider_verse.add_cannon_event(2)
        spider_verse.add_connection(0, 1)
        spider_verse.remove_connection(0, 1)
        spider_verse.show_multiverse()
        self.assertEqual(spider_verse.multiverse,
                         [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
