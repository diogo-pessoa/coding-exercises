class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self, data):
        node = Node(data)
        self.head = node
        self.tail = node
        self.size = 1

    def append(self, data):
        """
        O(1)
        :param data:
        :return:
        """
        new_node = Node(data)

        self.tail.next = new_node  # current tail points to new node
        new_node.prev = self.tail  # new node previous points to current tail
        self.tail = new_node  # update ll tail to new node
        self.size += 1  # bump size

    def pop(self):
        """
        O(1)
        :return:
        """

        if self.size == 0:
            return None
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return None
        new_tail = self.head
        while new_tail.next is not self.tail:
            new_tail = new_tail.next
        self.tail = new_tail
        self.tail.next = None

        return True
