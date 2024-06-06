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
        self.assertEqual(d_linked_list.size, 2)

    @unittest.skip("Not implemented")
    def test_append_empty_list(self):
        d_linked_list = DoublyLinkedList(10)
        d_linked_list.append(20)
        self.assertEqual(d_linked_list.head.next.data, 20)
        self.assertEqual(d_linked_list.tail.prev.data, 10)
        self.assertEqual(d_linked_list.size, 2)

    def test_pop(self):
        d_linked_list = DoublyLinkedList(10)
        d_linked_list.append(20)
        d_linked_list.append(30)
        d_linked_list.pop()
        self.assertEqual(d_linked_list.tail.data, 20)
        self.assertEqual(d_linked_list.tail.next, None)
        self.assertEqual(d_linked_list.tail.prev.data, 10)
        self.assertEqual(d_linked_list.size, 2)

    def test_pop_one_element(self):
        d_linked_list = DoublyLinkedList(10)
        d_linked_list.pop()
        self.assertEqual(d_linked_list.tail, None)
        self.assertEqual(d_linked_list.head, None)
        self.assertEqual(d_linked_list.size, 0)

    def test_prepend(self):
        d_linked_list = DoublyLinkedList(10)
        d_linked_list.prepend(5)
        self.assertEqual(d_linked_list.head.data, 5)
        self.assertEqual(d_linked_list.head.next.data, 10)
        self.assertEqual(d_linked_list.head.next.prev.data, 5)
        self.assertEqual(d_linked_list.size, 2)

    def test_pop_first(self):
        d_linked_list = DoublyLinkedList(10)
        d_linked_list.append(20)
        d_linked_list.append(30)
        d_linked_list.pop_first()
        self.assertEqual(d_linked_list.head.data, 20)
        self.assertEqual(d_linked_list.head.prev, None)
        self.assertEqual(d_linked_list.size, 2)

    def test_str_method(self):
        d_linked_list = DoublyLinkedList(10)
        d_linked_list.append(20)
        d_linked_list.append(30)
        print(d_linked_list)
        self.assertEqual(str(d_linked_list), "10 -> 20 -> 30")

    def test_get_node(self):
        """
        Running this test with the Debugger helps to see the iteration through head or tail
        :return:
        """
        d_linked_list = DoublyLinkedList(10)
        d_linked_list.append(20)
        d_linked_list.append(30)
        self.assertEqual(d_linked_list.get_node(1).data, 20)
        self.assertEqual(d_linked_list.get_node(2).data, 30)
        self.assertEqual(d_linked_list.get_node(0).data, 10)
        self.assertEqual(d_linked_list.get_node(3), None)
