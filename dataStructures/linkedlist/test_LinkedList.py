from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from dataStructures.linkedlist.LinkedList import LinkedList


class TestLinkedList(TestCase):

    def test_ll_creation(self):
        linked_list = LinkedList(4)
        self.assertEqual(linked_list.head.data, 4)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_list(self, mock_stdout):
        linked_list = LinkedList(3)
        linked_list.print_list()
        self.assertEqual(mock_stdout.getvalue().strip(), '3')

    def test_prepend_ll(self):
        linked_list = LinkedList(3)
        linked_list.prepend(2)
        self.assertEqual(linked_list.get_head().data, 2)
        self.assertEqual(linked_list.get_head().next, 3)

    def test_append_ll(self):
        linked_list = LinkedList(3)
        linked_list.append(2)
        self.assertEqual(linked_list.get_tail().data, 2)

    def test_pop_ll(self):
        linked_list = LinkedList(3)
        linked_list.append(2)
        linked_list.pop()
        self.assertEqual(linked_list.get_tail().data, 3)
        self.assertEqual(linked_list.get_tail().next, None)

    def test_ll_empty(self):
        linked_list = LinkedList(3)
        linked_list.pop()
        self.assertTrue(linked_list.is_empty())

    def test_pop_head_ll(self):
        linked_list = LinkedList(3)
        linked_list.append(2)
        linked_list.append(4)
        linked_list.pop_head()
        self.assertEqual(linked_list.get_head().data, 2)
        self.assertEqual(linked_list.get_head().next.data, 4)

    def test_get_head(self):
        self.assertEqual(LinkedList(3).get_head().data, 3)

    def test_get_tail(self):
        self.assertEqual(LinkedList(3).get_tail().data, 3)

    def test_get_length(self):
        linked_list = LinkedList(3)
        linked_list.append(2)
        linked_list.append(4)
        self.assertEqual(linked_list.get_length(), 3)

    def test_get_by_index(self):
        linked_list = LinkedList(3)
        linked_list.append(2)
        linked_list.append(4)
        self.assertEqual(linked_list.get_by_index(1).data, 2)

    def test_update_node_value(self):
        linked_list = LinkedList(3)
        linked_list.append(2)
        linked_list.append(4)
        linked_list.update_node_value(1, 5)
        self.assertEqual(linked_list.get_by_index(1).data, 5)

    def test_insert_new_node(self):
        linked_list = LinkedList(3)
        linked_list.append(2)
        linked_list.append(4)
        linked_list.insert_new_node(5, 1)
        self.assertEqual(linked_list.get_by_index(1).data, 5)

    def test_remove_node(self):
        linked_list = LinkedList(3)
        linked_list.append(2)
        linked_list.append(4)
        linked_list.remove(1)
        self.assertEqual(linked_list.get_by_index(1).data, 4)

    def test_reverse_ll(self):
        linked_list = LinkedList(3)
        linked_list.append(2)
        linked_list.append(4)
        linked_list.print_list()
        linked_list.reverse()
        linked_list.print_list()
        self.assertEqual(linked_list.get_by_index(0).data, 4)
        self.assertEqual(linked_list.get_by_index(1).data, 2)
        self.assertEqual(linked_list.get_by_index(2).data, 3)

    def test_find_middle_node(self):
        my_linked_list = LinkedList(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.append(4)
        my_linked_list.append(5)
        self.assertEqual(my_linked_list.find_middle_node().data, 3)

    def test_find_middle_node_even_number(self):
        my_linked_list = LinkedList(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.append(4)
        self.assertEqual(my_linked_list.find_middle_node().data, 3)
