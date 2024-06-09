from unittest import TestCase

from dataStructures.graph.GraphAdList import GraphAdjList


class TestGraphAdjList(TestCase):
    def test_add_cannon(self):
        spider_verse = GraphAdjList()
        spider_verse.add_canon_event(1)
        self.assertEqual(spider_verse.graph, {1: []})

    def test_add_connections(self):
        spider_verse = GraphAdjList()
        spider_verse.add_canon_event(1)
        spider_verse.add_canon_event(2)
        spider_verse.add_connection(1, 2)
        self.assertEqual(spider_verse.graph, {1: [2], 2: [1]})

    def test_remove_connection(self):
        spider_verse = GraphAdjList()
        spider_verse.add_canon_event(1)
        spider_verse.add_canon_event(2)
        spider_verse.add_connection(1, 2)
        spider_verse.remove_connection(1, 2)
        spider_verse.show_multiverse()
        self.assertEqual(spider_verse.graph, {1: [], 2: []})

    def test_remove_cannon(self):
        spider_verse = GraphAdjList()
        spider_verse.add_canon_event(1)
        spider_verse.add_canon_event(2)
        spider_verse.add_connection(1, 2)
        spider_verse.remove_canon_event(1)
        self.assertEqual(spider_verse.graph, {2: []})
