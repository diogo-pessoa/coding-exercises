from dataStructures.tree.Node import Node


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        O(log n) time complexity
        O(1) space complexity
        :param value:
        :return:
        """
        root = self.root
        if not root:
            self.root = Node()
            self.root.data = value
            return self.root

        while True:
            if value > root.data:
                if root.right is None:
                    root.right = Node()
                    root.right.data = value
                    return root.right
                root = root.right
            elif value < root.data:
                if root.left is None:
                    root.left = Node()
                    root.left.data = value
                    return root.left
                root = root.left
            else:
                return None  # or some appropriate value

    def contains(self, value):
        """
        O(log n) time complexity
        O(1) space complexity
        :param value:
        :return:
        """
        root = self.root
        while root:
            if value > root.data:
                root = root.right
            elif value < root.data:
                root = root.left
            else:
                return True
        return False
