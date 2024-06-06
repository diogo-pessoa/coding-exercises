import unittest
from unittest import TestCase

from dataStructures.doublylinkedlist.DoublyLinkedList import DoublyLinkedList


class TestDoublyLinkedList(TestCase):

    def test_init(self):
        d_linked_list = DoublyLinkedList(10)
        self.assertEqual(d_linked_list.head.data, 10)

    def test_append(self):
        d_linked_list = DoublyLinkedList(10)
        d_linked_list.append(20)
        self.assertEqual(d_linked_list.head.next.data, 20)
        self.assertEqual(d_linked_list.tail.prev.data, 10)

    @unittest.skip("Not implemented")
    def test_append_empty_list(self):
        d_linked_list = DoublyLinkedList(10)
        d_linked_list.append(20)
        self.assertEqual(d_linked_list.head.next.data, 20)

    def test_pop(self):
        d_linked_list = DoublyLinkedList(10)
        d_linked_list.append(20)
        d_linked_list.append(30)
        d_linked_list.pop()
        self.assertEqual(d_linked_list.tail.data, 20)
        self.assertEqual(d_linked_list.tail.next, None)
        self.assertEqual(d_linked_list.tail.prev.data, 10)

    def test_pop_one_element(self):
        d_linked_list = DoublyLinkedList(10)
        d_linked_list.pop()
        self.assertEqual(d_linked_list.tail, None)
        self.assertEqual(d_linked_list.head, None)
        self.assertEqual(d_linked_list.size, 0)