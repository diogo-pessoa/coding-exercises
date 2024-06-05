class Node:
    def __init__(self, value):
        """
        Initialize the Node with a value, and the reference to the next node.
        :param value:
        """
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self, data):
        """
        The LL constructor is creating a new node,
        setting the head and tail of the LL to the new node
        We also set the length to 1.
        :param data:
        """
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, data):
        """
        Add value to end of LL.
        - Need to update last element (tail)
        - bump the length
        - update former tail to have .next as new tail.

        :param data:
        :return:
        """

        new_node = Node(data)
        if not self.head:  # if list is empty.
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self.tail

    def prepend(self, data):
        """
        Adding a new node to the beginning of the LL
        - move head data to new node
        - set next value to former head
        - increment the length of the ll
        :param data:
        :return: node: Node
        """
        new_node = Node(data)
        if not self.head:  # if list is empty.
            self.head = new_node
            self.tail = new_node

        node = Node(data)
        node.next = self.head.data
        self.head = node
        self.length += 1
        return node

    def pop(self):
        """
        Update new tail by checking if .next in element is current self.tail.
        :return:
        """
        if not self.head or self.length <= 1:
            self.head = self.tail = None
            self.length = 0
        else:
            new_tail = self.head
            while new_tail.next is not self.tail:
                new_tail = new_tail.next
            self.tail = new_tail
            self.tail.next = None
        return self.tail

    def print_list(self):
        """
        Prints all elements in the list.
        Starting from the head element and updating the node with .next until tail element (next will be None)
        :return: None
        """
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
