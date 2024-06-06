from unittest import TestCase

from dataStructures.tree.BinarySearchTree import BinarySearchTree


class TestBinarySearchTree(TestCase):

    def test_insert_right(self):
        binary_tree = BinarySearchTree()
        binary_tree.insert(3)
        binary_tree.insert(5)
        self.assertEqual(binary_tree.root.right.data, 5)

    def test_insert_left(self):
        binary_tree = BinarySearchTree()
        binary_tree.insert(3)
        binary_tree.insert(1)
        self.assertEqual(binary_tree.root.left.data, 1)

    def test_insert_root(self):
        binary_tree = BinarySearchTree()
        binary_tree.insert(3)
        self.assertEqual(binary_tree.root.data, 3)

    def test_insert_duplicate(self):
        binary_tree = BinarySearchTree()
        binary_tree.insert(3)
        binary_tree.insert(3)
        self.assertEqual(binary_tree.root.data, 3)

    def test_contains(self):
        binary_tree = BinarySearchTree()
        binary_tree.insert(3)
        binary_tree.insert(5)
        self.assertTrue(binary_tree.contains(5))
