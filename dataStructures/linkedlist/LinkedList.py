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

    def get_by_index(self, index):
        """
        O(n)
        :param index:
        :return:
        """
        if index < 0 or index >= self.length:  # remember to validate the index is within length of LL
            return None
        node = self.head
        for i in range(index):
            node = node.next
        return node

    def get_head(self):
        return self.head if self.head else None

    def get_tail(self):
        return self.tail if self.tail else None

    def get_length(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def update_node_value(self, index, data):
        """
        O(n)
        :param index:
        :param data:
        :return:
        """
        if index < 0 or index >= self.length:
            return None
        node = self.get_by_index(index)  # O(n) using the get_by_index method to get the node
        if node:  # if node is found, update the data
            node.data = data  # update the data of the node
        return node

    def insert_new_node(self, data, index):
        """
        O(n)
        :param data:
        :param index:
        :return:
        """
        if index < 0 or index >= self.length:  # Index Out of Bounds
            return None
        if index == self.length:  # Inserting at the end of the LL
            return self.append(data)  # O(1)

        if index == 0:  # First element in LL
            return self.prepend(data)  # O(1)

        # Inserting in the middle of the LL
        new_node = Node(data)
        node = self.get_by_index(index - 1)  # O(n)
        new_node.next = node.next
        node.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """
        For the return value it made sense to return the removed node, instead of a Boolean.
        In cases the client uses this values later.
        O(n)
        :returns: removed_node: Node or None
        """
        if index < 0 or index >= self.length:  # Index Out of Bounds
            return None
        if index == 0:  # First element in LL
            return self.pop_head()
        if index == self.length - 1:  # Last element in LL
            return self.pop()
        previous_node_in_ll = self.get_by_index(index - 1)  # O(n)
        removed_node = previous_node_in_ll.next
        previous_node_in_ll.next = removed_node.next  # O(1) - Updating the next value of preceding deleted node
        self.length -= 1
        return removed_node

    def reverse(self):
        """
        O(n) - Need to iterate through the whole list to reverse the order of the nodes.

        :return:
        """
        previous = None
        current = self.head  # Starting at the first node
        self.tail = self.head  # setting the last node as the former head
        while current is not None:  # Tail node doesnt a .next value
            next_node = current.next
            current.next = previous  # first interation will be None
            previous = current
            current = next_node
        self.head = previous

    def append(self, data):
        """
        O(1)
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
        return True

    def pop(self):
        """
        O(1) - worst case we navigate the whole list, see while l.57
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
        return self.tail  # returning the removed tail node

    def prepend(self, data):
        """
        O(1)
        Adding a new node to the beginning of the LL
        - move head data to new node
        - set next value to former head
        - increment the length of the ll
        :param data:
        """
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            node = Node(data)
            node.next = self.head.data
            self.head = node
            self.length += 1
        return True

    def pop_head(self):
        """
        O(1)
        :return: head_node: returns the removed head node
        """
        removed_head = self.head
        new_head = self.head.next
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return None

        self.head = new_head
        self.length -= 1
        return removed_head  # returning the removed head node

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
