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

