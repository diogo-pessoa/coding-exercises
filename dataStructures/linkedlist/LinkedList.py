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

    def prepend(self, data):
        """
        Adding a new node to the beginning of the LL
        :param data:
        :return:
        """
        pass

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